from pydantic import BaseModel
from typing import Optional
class RegisterModel(BaseModel):
    username:Optional[str]
    email:str
    password:str

class LoginModel(BaseModel):
    username:Optional[str]
    email:str
    password:str
