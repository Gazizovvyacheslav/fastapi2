from pydantic import BaseModel, Field, ConfigDict


class CreateTask(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: str | None = None


class UpdateTask(BaseModel):
    is_done: bool

class ReadTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int 
    title: str = Field(min_length=1, max_length=150)
    description: str | None = None
    is_done: bool
