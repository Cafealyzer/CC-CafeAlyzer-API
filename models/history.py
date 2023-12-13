from datetime import datetime
from beanie import Document
from pydantic import Field

class History(Document):
  username: str = Field(...)
  cafeUser: str = Field(...)
  cafeCompetitor: str = Field(...)
  date: datetime
  positiveFeedback: list = Field(...)
  negativeFeedback: list = Field(...)
  positiveFeedbackCompetitor: list = Field(...)
  negativeFeedbackCompetitor: list = Field(...)
  suggestion: list = Field(...)

  class Config:
    json_schema_extra = {
      "example": {
        "username": "zikri",
        "cafeUser": "fusion cafe",
        "cafeCompetitor": "starbucks",
        "date": "2020-10-18T00:00:00Z",
        "positiveFeedback": ["good coffee", "good service"],
        "negativeFeedback": ["bad coffee", "bad service"],
        "positiveFeedbackCompetitor": ["good coffee", "good service"],
        "negativeFeedbackCompetitor": ["bad coffee", "bad service"],
        "suggestion": ["more coffee", "more service"]
      }
    }
    
  class Settings:
    name = "history"