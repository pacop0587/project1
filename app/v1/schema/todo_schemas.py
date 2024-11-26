from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str
    done: bool
    user_id: int

    class Config:
        orm_mode = True

class TodoRequest(TodoBase):
    class Config:
        orm_mode = True

class TodoResponse(TodoBase):
    id:int
    class Config:
        orm_mode = True