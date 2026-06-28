from backend.services.exceptions import (
    SearchRequestError,
    FetchRequestError,
    HTMLCleaningError,
)

errors = [
    SearchRequestError("Search failed"),
    FetchRequestError("Could not fetch webpage"),
    HTMLCleaningError("Cleaner failed"),
]

for error in errors:
    try:
        raise error
    except Exception as e:
        print(type(e).__name__)
        print(e)
        print("-" * 40)