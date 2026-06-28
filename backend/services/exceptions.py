class LLMServiceError(Exception):
    """
    Raised when communication with the local LLM fails.
    """

    pass

class SQSError(Exception):
    """
    Base exception for the Smart Quote System.
    """

    pass

class SearchError(SQSError):
    """
    Base exception for all search-related errors.
    """

    pass

class SearchConfigurationError(SearchError):
    """
    Raised when a search provider is misconfigured.
    """

    pass

class SearchRequestError(SearchError):
    """
    Raised when the search request fails.
    """

    pass

class SearchResponseError(SearchError):
    """
    Raised when the provider returns invalid data.
    """

    pass

class FetchError(SQSError):
    """
    Base exception for webpage fetching.
    """

    pass

class FetchRequestError(FetchError):
    """
    Raised when downloading a webpage fails.
    """

    pass

class InvalidPageError(FetchError):
    """
    Raised when fetched page content is invalid.
    """

    pass

class CleanerError(SQSError):
    """
    Base exception for HTML cleaning.
    """

    pass

class HTMLCleaningError(CleanerError):
    """
    Raised when HTML cleaning fails.
    """

    pass

class TrimmerError(SQSError):
    """
    Base exception for content trimming.
    """

    pass

