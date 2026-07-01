from backend.models.product_specifications import ProductSpecifications
from backend.services.extraction.prompt_builder import PromptBuilder
from backend.services.extraction.response_parser import ResponseParser
from backend.services.llm_service import LLMService
from typing import Optional

class SpecificationExtractor:
    """
    Extracts structured product specifications using an LLM.
    """

    def __init__(
        self,
        llm_service: Optional[LLMService] = None,
        prompt_builder: Optional[PromptBuilder] = None,
        response_parser: Optional[ResponseParser] = None,
    ):
        self.llm_service = llm_service or LLMService()

        self.prompt_builder = (
            prompt_builder
            or PromptBuilder()
        )

        self.response_parser = (
            response_parser
            or ResponseParser()
        )
    def extract(
        self,
        product_name: str,
        content: str,
    ) -> ProductSpecifications:
        """
        Extract specifications from cleaned product content.
        """

        messages = self.prompt_builder.build_messages(
            product_name,
            content,
        )

        response = self.llm_service.generate(messages)

        return self.response_parser.parse(
            response.content,
        )