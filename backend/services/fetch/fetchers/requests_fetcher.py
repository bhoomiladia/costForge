from urllib.parse import urlparse

import requests

from backend.models.search_result import SearchResult
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
            "User-Agent": self.USER_AGENT
        }
    def fetch(self, search_result: SearchResult) -> WebPage:
        """
        Fetch a webpage from a search result.
        """

        response = requests.get(
            str(search_result.url),
            headers=self._headers(),
            timeout=self.REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        return WebPage(
            url=search_result.url,
            source_domain=search_result.source_domain,
            title=search_result.title,
            html=response.text,
        )