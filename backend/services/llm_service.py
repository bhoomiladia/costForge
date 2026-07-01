from typing import Optional
import requests
from backend.models.llm_response import LLMResponse
from backend.services.exceptions import LLMServiceError

class LLMService:
    """
    Service responsible for communicating with local LLMs
    through the LM Studio OpenAI-compatible API.
    """

    def __init__(
        self,
        base_url: str = "http://localhost:1234/v1",
        model: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 2048,
        timeout: int = 120,
    ):
        """
        Initialize the LLM service.

        Args:
            base_url: LM Studio OpenAI-compatible API endpoint.
            model: Name of the model to use. If None, LM Studio's currently loaded model is used.
            temperature: Sampling temperature.
            max_tokens: Maximum number of tokens to generate.
            timeout: Request timeout in seconds.
        """

        self.base_url = base_url.rstrip("/")
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout

    @property
    def chat_endpoint(self) -> str:
        """
        Returns the full Chat Completions endpoint.
        """
        return f"{self.base_url}/chat/completions"

    def is_available(self) -> bool:
        """
        Check whether the LM Studio server is reachable.
        """

        try:
            response = requests.get(
                f"{self.base_url}/models",
                timeout=5
        )

            return response.status_code == 200

        except requests.RequestException:
            return False
    def generate(
        self,
        messages: list[dict[str, str]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> LLMResponse:
        """
        Send chat messages to the local LLM and return the response.
        """

        payload = {
            "messages": messages,
            "temperature": (
                temperature
                if temperature is not None
                else self.temperature
            ),
            "max_tokens": (
                max_tokens
                if max_tokens is not None
                else self.max_tokens
            ),
        }

        selected_model = model if model is not None else self.model

        if selected_model:
            payload["model"] = selected_model

        try:
            response = requests.post(
                self.chat_endpoint,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()
            data = response.json()

        except requests.exceptions.Timeout:
            raise LLMServiceError(
                "Request to the local LLM timed out."
            )

        except requests.exceptions.ConnectionError:
            raise LLMServiceError(
                "Could not connect to LM Studio. Is the local server running?"
            )

        except requests.exceptions.HTTPError as e:
            raise LLMServiceError(
                f"HTTP error from LM Studio: {e}"
            )

        except requests.exceptions.RequestException as e:
            raise LLMServiceError(
                f"Unexpected request error: {e}"
            )

        except ValueError:
            raise LLMServiceError(
                "LM Studio returned an invalid JSON response."
            )

        try:
            message = data["choices"][0]["message"]
        except (KeyError, IndexError):
            raise LLMServiceError(
                "Invalid response format returned by the LLM."
            )
        usage = data.get("usage", {})
        reasoning = message.get("reasoning_content")

        if reasoning:
            reasoning = reasoning.strip()

        return LLMResponse(
            content=message.get("content", "").strip(),
            reasoning=reasoning,
            model=data.get("model", "unknown"),
            finish_reason=data["choices"][0].get("finish_reason", "unknown"),
            prompt_tokens=usage.get("prompt_tokens", 0),
            completion_tokens=usage.get("completion_tokens", 0),
            reasoning_tokens=usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0),
            total_tokens=usage.get("total_tokens", 0),
        )