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

class ResponseLogin(BaseModel):
  status_code: int
  description: str
  token: object

  class Config:
    json_schema_extra = {
      "example": {
        "status_code": 200,
        "description": "Login Successfull",
        "token": "Sample Token",
      }
    }