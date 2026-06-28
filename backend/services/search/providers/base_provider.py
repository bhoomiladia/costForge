from abc import ABC, abstractmethod

from backend.models.search_result import SearchResult

class BaseSearchProvider(ABC):
    """
    Abstract base class for all web search providers.
    """

    @abstractmethod
    def search(self, query: str) -> list[SearchResult]:
        """
        Execute a web search and return normalized search results.
        """
        self._validate()
        return []