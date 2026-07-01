from abc import ABC, abstractmethod

from pydantic import HttpUrl

from backend.models.web_page import WebPage


class BaseFetcher(ABC):
    """
    Base interface for webpage fetchers.
    """

    @abstractmethod
    def fetch(
        self,
        url: HttpUrl,
    ) -> WebPage:
        pass