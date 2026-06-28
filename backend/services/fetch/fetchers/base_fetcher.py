from abc import ABC, abstractmethod

from backend.models.web_page import WebPage
from backend.models.search_result import SearchResult

class BaseFetcher(ABC):
    """
    Abstract base class for webpage fetchers.
    """

    @abstractmethod
    def fetch(self, search_result: SearchResult) -> WebPage:
        """
        Fetch a webpage from a search result.
        """
        pass