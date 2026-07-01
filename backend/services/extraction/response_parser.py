import json

from backend.models.product_specifications import ProductSpecifications
from backend.services.exceptions import LLMResponseParseError


class ResponseParser:
    """
    Parses the LLM response into a ProductSpecifications object.
    """

    def parse(
        self,
        response: str,
    ) -> ProductSpecifications:
        """
        Parse the JSON returned by the LLM.
        """

        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:
            raise LLMResponseParseError(
                f"Invalid JSON returned by LLM: {e}"
            )

        try:
            return ProductSpecifications(**data)

        except Exception as e:
            raise LLMResponseParseError(
                f"Invalid product specification format: {e}"
            )