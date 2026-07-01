from typing import Optional
import requests
from backend.models.search_result import SearchResult
from backend.models.web_page import WebPage
from backend.services.fetch.fetchers.base_fetcher import BaseFetcher
from backend.services.fetch.fetchers.requests_fetcher import RequestsFetcher

BLACKLIST = {
    "reddit.com",
    "youtube.com",
    "youtu.be",
}

class PageFetchService:
    """
    Service responsible for downloading web pages.
    """

    def __init__(
        self,
        fetcher: Optional[BaseFetcher] = None,
    ):
        self.fetcher = fetcher or RequestsFetcher()

    def fetch(
        self,
        search_results: list[SearchResult],
        max_pages: int = 3,
    ) -> list[WebPage]:
        """
        Fetch all pages from search results.
        """

        pages = []

        for result in search_results:

            if any(
                result.source_domain.endswith(domain)
                for domain in BLACKLIST
            ):
                continue

            try:
                page = self.fetcher.fetch(result.url)

                if page:
                    pages.append(page)

                if len(pages) >= max_pages:
                    break
            except requests.RequestException as e:
                print(f"Skipping {result.url}: {e}")

        return pages