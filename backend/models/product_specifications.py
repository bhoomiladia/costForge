from typing import Dict
from pydantic import BaseModel

class ProductSpecifications(BaseModel):
    """
    Raw specifications collected from external sources.
    """

    product_name: str

    source: str

    specifications: Dict[str, str]
    