"""
Prompt templates used for specification extraction.
"""

SYSTEM_PROMPT = """

/no_think

You are an expert information extraction engine.

Your task is to extract structured product specifications from the provided text.

Rules:

- Extract ONLY information explicitly present in the text.
- Never infer, guess, or hallucinate values.
- If a field is missing, return null.
- Return ONLY valid JSON.
- Do not wrap the JSON in markdown.
- Do not explain your reasoning.
- Do not include any text before or after the JSON.
- Preserve values exactly as written whenever possible.
- Lists should be returned as JSON arrays.
"""

USER_PROMPT = """
Extract the product specifications from the text below.

Return JSON using EXACTLY this schema:

{{
    "product_name": string | null,
    "brand": string | null,
    "model": string | null,
    "category": string | null,

    "processor": string | null,
    "gpu": string | null,
    "memory": string | null,
    "storage": string | null,
    "display": string | null,
    "battery": string | null,
    "camera": string | null,

    "wireless": string | null,
    "ports": [string],

    "dimensions": string | null,
    "weight": string | null,
    "materials": string | null,
    "colors": [string],

    "operating_system": string | null,

    "price": string | null,
    "release_date": string | null,

    "special_features": [string]
}}

Product Name:
{product_name}

Content:
{content}
"""