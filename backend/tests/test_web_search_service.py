from backend.services.search.providers.serper_provider import SerperProvider
from backend.services.search.web_search_service import WebSearchService

provider = SerperProvider()

search_service = WebSearchService(provider)

results = search_service.search("iPhone 15")

print(f"Found {len(results)} results")

for result in results[:3]:
    print(result.title)