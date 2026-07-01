from typing import Optional
from pydantic import Field
from backend.models.base_schema import BaseSchema


class ProductSpecifications(BaseSchema):
    """
    Structured specifications extracted from product webpages.
    """

    product_name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    category: Optional[str] = None

    processor: Optional[str] = None
    gpu: Optional[str] = None
    memory: Optional[str] = None
    storage: Optional[str] = None
    display: Optional[str] = None
    battery: Optional[str] = None
    camera: Optional[str] = None

    wireless: Optional[str] = None
    

    dimensions: Optional[str] = None
    weight: Optional[str] = None
    materials: Optional[str] = None
    

    operating_system: Optional[str] = None

    price: Optional[str] = None
    release_date: Optional[str] = None          

    ports: list[str] = Field(default_factory=list)

    colors: list[str] = Field(default_factory=list)

    special_features: list[str] = Field(default_factory=list)