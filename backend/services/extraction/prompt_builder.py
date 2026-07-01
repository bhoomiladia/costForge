from backend.services.extraction.prompts import (
    SYSTEM_PROMPT,
    USER_PROMPT,
)


class PromptBuilder:
    """
    Builds prompts for specification extraction.
    """

    def build_messages(
        self,
        product_name: str,
        content: str,
    ) -> list[dict[str, str]]:
        """
        Build chat messages for the LLM.
        """

        return [
            {
                "role": "system",
                "content": self._build_system_prompt(),
            },
            {
                "role": "user",
                "content": self._build_user_prompt(
                    product_name,
                    content,
                ),
            },
        ]

    def _build_system_prompt(self) -> str:
        """
        Build the system prompt.
        """

        return SYSTEM_PROMPT

    def _build_user_prompt(
        self,
        product_name: str,
        content: str,
    ) -> str:
        """
        Build the user prompt.
        """

        return USER_PROMPT.format(
            product_name=product_name,
            content=content,
        )