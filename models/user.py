from typing import Optional, Any
from beanie import Document, Indexed, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from fastapi.security import HTTPBasicCredentials

class User(Document):
  username: str = Field(...)
  email: EmailStr
  password: str = Field(...)
  
  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe",
        "email": "johndoe@gmail.com",
        "password": "secret"
      }
    }
  
  class Settings:
    name = "user"

class UpdateUser(BaseModel):
  username: Optional[str]
  email: Optional[EmailStr]
  password: Optional[str]

  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoee",
        "email": "johndoe@gmail.com",
        "password": "secret"
      }
    }

class UserLogin(HTTPBasicCredentials):
  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe", 
        "password": "secret"
      }
    }

class UserData(BaseModel):
  _id = PydanticObjectId
  username: str = Field(...)
  email: EmailStr
  
  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe",
        "email": "johndoe@gmail.com",
      }
    }

class Response(BaseModel):
  status_code: int
  response_type: str
  description: str
  data: Optional[Any]

  class Config:
    json_schema_extra = {
      "example": {
          "status_code": 200,
          "response_type": "success",
          "description": "Operation successful",
          "data": "Sample data",
      }
    }

