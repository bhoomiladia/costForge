from backend.services.extraction.response_parser import ResponseParser

parser = ResponseParser()

response = """
{
    "product_name": "HP Laptop",
    "processor": "Intel Core Ultra 7",
    "memory": "16GB RAM",
    "ports": ["USB-C"]
}
"""

specs = parser.parse(response)

print(type(specs))
print(specs)
print(specs.processor)
print(specs.memory)
print(specs.ports)