from backend.models.product import Product, ProductCategory

product = Product(
    canonical_name="Apple iPhone 15",
    brand="Apple",
    category=ProductCategory.SMARTPHONE,
    model="iPhone 15",
    aliases=["iphone15"],
    verified=True,
    confidence=99
)

print(product.model_dump())