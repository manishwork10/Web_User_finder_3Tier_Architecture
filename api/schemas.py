from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    phonenumber: str

class UserOut(BaseModel):
    username: str
    phonenumber: str