from datetime import datetime
from beanie import Document
from pydantic import Field

class History(Document):
  username: str = Field(None)
  cafeUser: str = Field(...)
  cafeCompetitor: str = Field(...)
  date: datetime = Field(None)
  positiveFeedback: list = Field(...)
  negativeFeedback: list = Field(...)
  positiveFeedbackCompetitor: list = Field(...)
  negativeFeedbackCompetitor: list = Field(...)
  suggestion: list = Field(...)

  class Config:
    json_schema_extra = {
      "example": {
        "cafeUser": "fusion cafe",
        "cafeCompetitor": "starbucks",
        "positiveFeedback": ["kopinya enak", "pelayanannya baik"],
        "negativeFeedback": ["teh nya kurang manis", "uang kembalian sobek"],
        "positiveFeedbackCompetitor": ["kopinya mantap", "harga terjangkau"],
        "negativeFeedbackCompetitor": ["jauh dari tempat saya"],
        "suggestion": ["Pastikan untuk tetap mempertahankan dan meningkatkan kualitas kopi agar pengalaman pengguna tetap memuaskan.", "Jangan lupakan untuk terus memberikan pelayanan yang ramah dan efisien kepada pelanggan.", "Pastikan untuk menjaga harga agar tetap bersaing dan memberikan nilai yang baik bagi pelanggan."]
      }
    }
    
  class Settings:
    name = "history"