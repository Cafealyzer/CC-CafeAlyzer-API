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

async def create_user_history(new_history: History) -> History:
  history = await new_history.create()
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