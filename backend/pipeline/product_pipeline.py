from typing import Optional

from backend.models.product_specifications import ProductSpecifications

from backend.services.search.web_search_service import WebSearchService

from backend.services.fetch.page_fetch_service import PageFetchService

from backend.services.cleaner.html_cleaner import HTMLCleaner
from backend.services.trimmer.content_trimmer import ContentTrimmer

from backend.services.extraction.specification_extractor import (
    SpecificationExtractor,
)

from backend.services.extraction.specification_merger import (
    SpecificationMerger,
)


class ProductPipeline:
    """
    End-to-end pipeline for discovering and extracting
    product specifications from the web.
    """

    def __init__(
        self,
        search_service: WebSearchService,
        fetch_service: Optional[PageFetchService] = None,
        cleaner: Optional[HTMLCleaner] = None,
        trimmer: Optional[ContentTrimmer] = None,
        extractor: Optional[SpecificationExtractor] = None,
        merger: Optional[SpecificationMerger] = None,
    ):
        self.search_service = search_service

        self.fetch_service = (
            fetch_service or
            PageFetchService()
        )

        self.cleaner = (
            cleaner or
            HTMLCleaner()
        )

        self.trimmer = (
            trimmer or
            ContentTrimmer()
        )

        self.extractor = (
            extractor or
            SpecificationExtractor()
        )

        self.merger = (
            merger or
            SpecificationMerger()
        )

    def run(
        self,
        query: str,
    ) -> ProductSpecifications:
        """
        Execute the complete extraction pipeline.
        """

        search_results = self.search_service.search(
            query
        )

        if not search_results:
            raise ValueError(
                f"No search results found for '{query}'."
            )

        pages = self.fetch_service.fetch(
            search_results
        )

        if not pages:
            raise ValueError(
                "Unable to fetch any webpages."
            )

        specifications: list[
            ProductSpecifications
        ] = []

        for page in pages:

            cleaned_text = self.cleaner.clean(page.html)

            trimmed_text = self.trimmer.trim(
                cleaned_text
            )

            if not trimmed_text.strip():
                continue

            specification = self.extractor.extract(
                product_name=query,
                content=trimmed_text,
            )

            specifications.append(
                specification
            )

        if not specifications:
            raise ValueError(
                "No specifications could be extracted."
            )

        return self.merger.merge(
            specifications
        )