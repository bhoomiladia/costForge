from backend.services.search.providers.serper_provider import SerperProvider

provider = SerperProvider()

results = provider.search("Dell XPS 13")

print(f"Found {len(results)} results\n")

for result in results:
    print(result)
    print("-" * 80)