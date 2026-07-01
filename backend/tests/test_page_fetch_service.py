from backend.services.search.providers.serper_provider import SerperProvider
from backend.services.search.web_search_service import WebSearchService

from backend.services.fetch.fetchers.requests_fetcher import RequestsFetcher
from backend.services.fetch.page_fetch_service import PageFetchService


def main():
    # Step 1: Search for a product
    search_service = WebSearchService(
        provider=SerperProvider()
    )

    search_results = search_service.search("Dell XPS 13")

    print(f"Found {len(search_results)} search results.\n")

    # Step 2: Fetch the pages
    fetch_service = PageFetchService(
        fetcher=RequestsFetcher()
    )

    pages = fetch_service.fetch(search_results)

    print(f"Successfully fetched {len(pages)} pages.\n")

    # Step 3: Print summary
    for index, page in enumerate(pages, start=1):
        print("-" * 80)
        print(f"Page {index}")
        print(f"URL: {page.url}")
        print(f"Title: {page.title}")
        print(f"HTML Length: {len(page.html)} characters")
        print(page.html[:300].replace("\n", " "))
        print()


if __name__ == "__main__":
    main()
