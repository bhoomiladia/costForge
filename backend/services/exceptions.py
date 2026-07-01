"""
Custom exceptions used throughout the Smart Quote System (SQS).

Exception Hierarchy

Exception
│
└── SQSError
    │
    ├── LLMServiceError
    │
    ├── SearchError
    │   ├── SearchConfigurationError
    │   ├── SearchRequestError
    │   └── SearchResponseError
    │
    ├── FetchError
    │   ├── FetchRequestError
    │   └── InvalidPageError
    │
    ├── CleanerError
    │   └── HTMLCleaningError
    │
    ├── TrimmerError
    │   └── ContentTrimmingError
    │
    └── ExtractionError
        ├── SpecificationExtractionError
        └── InvalidExtractionError
"""


# ==========================================================
# Base Exception
# ==========================================================

class SQSError(Exception):
    """
    Base exception for the Smart Quote System.
    """

    pass


# ==========================================================
# LLM Exceptions
# ==========================================================

class LLMServiceError(SQSError):
    """
    Raised when the LLM service fails.
    """

    pass


# ==========================================================
# Search Exceptions
# ==========================================================

class SearchError(SQSError):
    """
    Base exception for all search-related errors.
    """

    pass


class SearchConfigurationError(SearchError):
    """
    Raised when a search provider is incorrectly configured.

    Examples:
    - Missing API key
    - Missing environment variable
    - Invalid endpoint
    """

    def __init__(self, provider: str, message: str):
        self.provider = provider
        super().__init__(f"[{provider}] {message}")


class SearchRequestError(SearchError):
    """
    Raised when a web search request fails.

    Examples:
    - Timeout
    - HTTP 429
    - HTTP 500
    - Network failure
    """

    def __init__(self, provider: str, message: str):
        self.provider = provider
        super().__init__(f"[{provider}] {message}")


class SearchResponseError(SearchError):
    """
    Raised when a search provider returns an invalid response.

    Examples:
    - Invalid JSON
    - Missing required fields
    - Unexpected response format
    """

    def __init__(self, provider: str, message: str):
        self.provider = provider
        super().__init__(f"[{provider}] {message}")


# ==========================================================
# Fetch Exceptions
# ==========================================================

class FetchError(SQSError):
    """
    Base exception for webpage fetching errors.
    """

    pass


class FetchRequestError(FetchError):
    """
    Raised when downloading a webpage fails.
    """

    def __init__(self, url: str, message: str):
        self.url = url
        super().__init__(f"[{url}] {message}")


class InvalidPageError(FetchError):
    """
    Raised when fetched page content is invalid.

    Examples:
    - Empty HTML
    - Unsupported content type
    - PDF instead of HTML
    """

    def __init__(self, url: str, message: str):
        self.url = url
        super().__init__(f"[{url}] {message}")


# ==========================================================
# HTML Cleaner Exceptions
# ==========================================================

class CleanerError(SQSError):
    """
    Base exception for HTML cleaning errors.
    """

    pass


class HTMLCleaningError(CleanerError):
    """
    Raised when HTML cleaning fails.
    """

    pass


# ==========================================================
# Content Trimmer Exceptions
# ==========================================================

class TrimmerError(SQSError):
    """
    Base exception for content trimming errors.
    """

    pass


class ContentTrimmingError(TrimmerError):
    """
    Raised when content trimming fails.
    """

    pass


# ==========================================================
# Specification Extraction Exceptions
# ==========================================================

class ExtractionError(SQSError):
    """
    Base exception for specification extraction.
    """

    pass


class SpecificationExtractionError(ExtractionError):
    """
    Raised when the LLM cannot extract structured specifications.
    """

    def __init__(self, product_name: str, message: str):
        self.product_name = product_name
        super().__init__(f"[{product_name}] {message}")


class InvalidExtractionError(ExtractionError):
    """
    Raised when extracted specifications fail validation.
    """

    pass 

class LLMResponseParseError(LLMServiceError):
    """
    Raised when the LLM response cannot be parsed.
    """