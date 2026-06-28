from backend.services.fetch.fetchers.requests_fetcher import RequestsFetcher
from backend.services.search.providers.serper_provider import SerperProvider

provider = SerperProvider()
results = provider.search("iPhone 15")

fetcher = RequestsFetcher()

page = fetcher.fetch(results[0])

print(page.title)
print(page.source_domain)
print(len(page.html))