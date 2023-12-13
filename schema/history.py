import datetime
from pydantic import BaseModel

class History(BaseModel):
  cafeUser: str
  cafeCompetitor: str
  date: datetime
  positiveFeedback: list
  negativeFeedback: list
  positiveFeedbackCompetitor: list
  negativeFeedbackCompetitor: list
  suggestion: list