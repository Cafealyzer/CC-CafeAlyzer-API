from pydantic import BaseModel
from typing import Optional, Any

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

class ResponseMe(BaseModel):
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
          "data": {
            "_id": "6563b9c4072f346b1a3c2425",
            "username": "username",
            "email": "email",
          },
      }
    }

class ResponseLogin(BaseModel):
  status_code: int
  description: str
  token: object

  class Config:
    json_schema_extra = {
      "example": {
        "status_code": 200,
        "description": "Login Successfull",
        "token": {
          "type": "bearer",
          "access_token": "token"
        },
      }
    }