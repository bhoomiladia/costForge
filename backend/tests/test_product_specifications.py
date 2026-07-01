from backend.models.product_specifications import ProductSpecifications


specs = ProductSpecifications(
    product_name="Dell XPS 13",
    processor="Intel Core Ultra 7",
    memory="16GB",
    ports=[
        "Thunderbolt 4",
        "USB-C",
    ],
)

print(specs)

print(specs.model_dump())