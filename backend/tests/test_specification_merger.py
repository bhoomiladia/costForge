from backend.models.product_specifications import ProductSpecifications
from backend.services.extraction.specification_merger import (
    SpecificationMerger,
)

spec1 = ProductSpecifications(
    product_name="HP Laptop",
    processor="Intel Core Ultra 7",
    battery="55 Wh",
    ports=["USB-C"],
)

spec2 = ProductSpecifications(
    memory="16GB RAM",
    storage="512GB SSD",
    ports=["Thunderbolt 4"],
)

spec3 = ProductSpecifications(
    weight="1.18 kg",
    colors=["Silver"],
    ports=["USB-C"],
)

merger = SpecificationMerger()

merged = merger.merge([
    spec1,
    spec2,
    spec3,
])

print(merged)