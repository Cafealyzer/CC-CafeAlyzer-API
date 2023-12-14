import datetime
from typing import List
from beanie import PydanticObjectId
from models.history import History
from .jwt import decode_jwt

history_collection = History

async def get_all_user_histories(token) -> List[History]:
  payload = decode_jwt(token)
  username: str = payload['username']
  histories = await history_collection.find(history_collection.username == username).to_list()
  return histories

async def create_user_history(new_history: History, token) -> History:
  username = decode_jwt(token)['username']

  history = History(
    _id=PydanticObjectId(),
    username=username,
    cafeUser=new_history.cafeUser,
    cafeCompetitor=new_history.cafeCompetitor,
    date=datetime.datetime.now(),
    positiveFeedback=new_history.positiveFeedback,
    negativeFeedback=new_history.negativeFeedback,
    positiveFeedbackCompetitor=new_history.positiveFeedbackCompetitor,
    negativeFeedbackCompetitor=new_history.negativeFeedbackCompetitor,
    suggestion=new_history.suggestion,
  )

  await history.save()

  return history

async def delete_user_history(id: PydanticObjectId) -> History:
  history = await history_collection.find_one(history_collection.id == id)
  await history.delete()
  return history

async def validation_history(id: PydanticObjectId) -> bool:
  history = await history_collection.find_one(history_collection.id == id)
  if history:
    return True
  return False