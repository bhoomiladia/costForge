from pydantic import BaseModel, HttpUrl

class WebPage(BaseModel):
    """
    Represents a fetched web page before any processing.
    """

    url: HttpUrl

    source_domain: str

    title: str

    html: str