from typing import List, Optional

from pydantic import  Field
from backend.models.base_schema import BaseSchema

class Component(BaseSchema):
    """
    Represents a single physical component of a product.
    """

    name: str

    quantity: int = Field(default=1, ge=1)