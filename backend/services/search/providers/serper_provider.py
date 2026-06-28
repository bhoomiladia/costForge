import os
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
from backend.models.search_result import SearchResult
from backend.services.search.providers.base_provider import BaseSearchProvider

load_dotenv()

class SerperProvider(BaseSearchProvider):
    """
    Web search provider powered by the Serper API.
    """
    PROVIDER_NAME = "serper"
    BASE_URL = "https://google.serper.dev/search"
    REQUEST_TIMEOUT = 30

    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")
    
    def _validate(self) -> None:
        """
        Ensure the provider is correctly configured.
        """

        if not self.api_key:
            raise ValueError(
                "SERPER_API_KEY environment variable is not set."
            )
        
    def _headers(self) -> dict[str,str]:
        """
        Build request headers.
        """

        return {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
        }
    def _payload(self, query: str) -> dict[str,str]:
        """
        Build the search payload.
        """

        return {
            "q": query
        }
    def search(self, query: str) -> list[SearchResult]:
        """
        Execute a web search using the Serper API.
        """

        self._validate()

        response = requests.post(
    self.BASE_URL,
    headers=self._headers(),
    json=self._payload(query),
    timeout=self.REQUEST_TIMEOUT,
)

        response.raise_for_status()

        response_data = response.json()

        search_results: list[SearchResult] = []
        organic_results = response_data.get("organic", [])

        if not organic_results:
            return []
        
        for organic_result in organic_results:
            link = organic_result.get("link", "")
            source_domain = urlparse(link).netloc
            search_result = SearchResult(
                title=organic_result.get("title", ""),
                url=link,
                snippet=organic_result.get("snippet", ""),
                provider=self.PROVIDER_NAME,
                source_domain=source_domain
            )

            search_results.append(search_result)

        return search_results

    

