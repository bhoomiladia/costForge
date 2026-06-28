from backend.models.search_result import SearchResult

result = SearchResult(
    title="Apple iPhone 15 - GSMArena",
    url="https://www.gsmarena.com/apple_iphone_15-12559.php",
    snippet="Apple iPhone 15 specifications...",
    provider="serper",
    relevance_score=0.96
)

print(result)