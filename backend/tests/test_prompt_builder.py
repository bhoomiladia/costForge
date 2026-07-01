from backend.services.extraction.prompt_builder import PromptBuilder

builder = PromptBuilder()

messages = builder.build_messages(
    "Dell XPS 13",
    "Processor: Intel Core Ultra 7",
)

for message in messages:
    print(message)