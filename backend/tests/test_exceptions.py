from backend.services.exceptions import LLMServiceError

try:
    raise LLMServiceError("Test error")
except LLMServiceError as e:
    print(e)