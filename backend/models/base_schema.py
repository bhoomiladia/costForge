from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Base class for all Pydantic models in the project.
    """

    model_config = ConfigDict(
        extra="ignore",
        validate_assignment=True,
    )