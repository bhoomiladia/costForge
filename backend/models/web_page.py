from pydantic import HttpUrl
from backend.models.base_schema import BaseSchema

class WebPage(BaseSchema):
    """
    Represents a fetched web page before any processing.
    """
    url: HttpUrl
    source_domain: str
    title: str
    html: str