from backend.services.extraction.specification_extractor import (
    SpecificationExtractor,
)

extractor = SpecificationExtractor()

specs = extractor.extract(
    "HP Laptop",
    """
Processor: Intel Core Ultra 7
Memory: 16GB RAM
Storage: 512GB SSD
Battery: 55 Wh
Display: 14-inch IPS
USB-C
Thunderbolt 4
""",
)

print(specs)
print()
print(specs.processor)
print(specs.memory)
print(specs.ports)