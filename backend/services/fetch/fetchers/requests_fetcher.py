from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from pydantic import HttpUrl

from backend.models.web_page import WebPage
from backend.services.fetch.fetchers.base_fetcher import BaseFetcher


class RequestsFetcher(BaseFetcher):
    """
    Fetch webpages using the requests library.
    """

    REQUEST_TIMEOUT = 30

    USER_AGENT = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )

    def _headers(self) -> dict[str, str]:
        return {
            "User-Agent": self.USER_AGENT,
        }

    def fetch(
        self,
        url: HttpUrl,
    ) -> WebPage:
        """
        Fetch a webpage from a URL.
        """

        response = requests.get(
            str(url),
            headers=self._headers(),
            timeout=self.REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = ""

        if soup.title:
            title = soup.title.get_text(strip=True)

        source_domain = urlparse(str(url)).netloc

        return WebPage(
            url=url,
            source_domain=source_domain,
            title=title,
            html=response.text,
        )