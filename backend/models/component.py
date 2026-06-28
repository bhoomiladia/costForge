from typing import List, Optional

from pydantic import BaseModel, Field

class Component(BaseModel):
    """
    Represents a single physical component of a product.
    """

    name: str

    quantity: int = Field(default=1, ge=1)