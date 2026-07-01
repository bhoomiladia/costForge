from typing import Optional

from pydantic import HttpUrl
from backend.models.base_schema import BaseSchema

class SearchResult(BaseSchema):
    """
    Represents a single search result returned by a web search provider.
    """

    title: str

    url: HttpUrl

    snippet: str

    provider: str
    
    source_domain: Optional[str] = None

    relevance_score: Optional[float] = None

