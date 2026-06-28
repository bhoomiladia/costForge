from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field


class ProductCategory(str, Enum):
    SMARTPHONE = "Smartphone"
    LAPTOP = "Laptop"
    TABLET = "Tablet"
    SMARTWATCH = "Smartwatch"
    EARBUDS = "Earbuds"
    HEADPHONES = "Headphones"
    MONITOR = "Monitor"
    TV = "TV"
    CAMERA = "Camera"
    OTHER = "Other"

class Product(BaseModel):
    """
    Canonical representation of a discovered product.
    This model is only responsible for storing product metadata.
    """

    canonical_name: str = Field(
        ...,
        description="Official product name after normalization."
    )

    brand: str = Field(
        ...,
        description="Manufacturer or brand."
    )

    category: ProductCategory = Field(
        ...,
        description="Product category such as Smartphone, Laptop, Tablet."
    )

    model: str = Field(
        ...,
        description="Specific model name."
    )

    aliases: List[str] = Field(
        default_factory=list,
        description="Alternative names entered by users."
    )

    verified: bool = Field(
        default=False,
        description="Whether the product has been verified."
    )

    confidence: Optional[float] = Field(
        default=None,
        ge=0,
        le=100,
        description="Verification confidence percentage."
    )
    model_config = {
    "use_enum_values": True,
    "validate_assignment": True,
    "extra": "forbid"
    }