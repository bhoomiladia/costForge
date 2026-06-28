from backend.services.llm_service import LLMService

llm = LLMService()

response = llm.generate(
    "What is 15 + 27?"
)

print(response)
print(response.content)
print(response.model)
print(response.total_tokens)
print(response.reasoning_tokens)