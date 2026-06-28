from backend.models.search_result import SearchResult
from backend.services.search.providers.base_provider import BaseSearchProvider

class WebSearchService:
    """
    High-level service for executing web searches.

    The service delegates all search operations to the configured
    search provider.
    """

    def __init__(self, provider: BaseSearchProvider):
        self.provider = provider

    def search(self, query: str) -> list[SearchResult]:
        """
        Execute a web search using the configured provider.
        """

        return self.provider.search(query)