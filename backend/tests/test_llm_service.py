from backend.services.extraction.prompt_builder import PromptBuilder
from backend.services.llm_service import LLMService


builder = PromptBuilder()
llm = LLMService()
messages = builder.build_messages(
    "HP Laptop",
    """
Processor: Intel Core Ultra 7
Memory: 16GB RAM
Storage: 512GB SSD
Battery: 55 Wh
Display: 14-inch IPS
USB-C
Thunderbolt 4
"""
)

response = llm.generate(messages)


print("\n=== LLM Response ===")
print(response)

print("\n=== Content ===")
print(response.content)

print("\n=== Model ===")
print(response.model)

print("\n=== Token Usage ===")
print(f"Prompt: {response.prompt_tokens}")
print(f"Completion: {response.completion_tokens}")
print(f"Reasoning: {response.reasoning_tokens}")
print(f"Total: {response.total_tokens}")