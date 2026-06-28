from backend.models.product_specifications import ProductSpecifications

specs = ProductSpecifications(
    product_name="Dell XPS 13",
    source="GSMArena",
    specifications={
        "Processor": "Intel Core Ultra 7",
        "RAM": "32 GB",
        "Storage": "1 TB SSD"
    }
)

print(specs)