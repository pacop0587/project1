from pydantic import BaseModel

class UserBase(BaseModel):
    email:str
    password:str
    is_active:bool

    class Config:
        orm_mode = True

class UserRequest(UserBase):
    class Config:
        orm_mode = True

class UserResponse(UserBase):
    id:int
    class Config:
        orm_mode = True
