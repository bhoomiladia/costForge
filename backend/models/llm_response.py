from typing import Optional

from pydantic import BaseModel

class LLMResponse(BaseModel):
    """
    Standard response returned by every local LLM call.
    """

    content: str

    reasoning: Optional[str] = None

    model: str

    finish_reason: str

    prompt_tokens: int

    completion_tokens: int

    reasoning_tokens: int = 0

    total_tokens: int