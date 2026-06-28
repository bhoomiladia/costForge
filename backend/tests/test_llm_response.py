from backend.models.llm_response import LLMResponse

response = LLMResponse(
    content="Hello",
    reasoning="Some reasoning",
    model="qwen/qwen3-8b",
    finish_reason="stop",
    prompt_tokens=12,
    completion_tokens=35,
    reasoning_tokens=20,
    total_tokens=47
)

print(response)