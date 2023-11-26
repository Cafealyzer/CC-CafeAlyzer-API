from fastapi import APIRouter, Body, Depends, dependencies, HTTPException
from beanie import PydanticObjectId
from passlib.context import CryptContext
from handlers.user import *
from models.user import *
from auth.jwt_bearer import JWTBearer
from handlers.user import get_current_user
from schema.response import Response

router = APIRouter()

token_listener = JWTBearer()

hash_helper = CryptContext(schemes=["bcrypt"])

@router.get("/", response_description="User retrieved", response_model=Response)
async def get_users():
  users = await get_all_users()
  print(users)
  return {
    "status_code": 200,
    "response_type": "success",
    "description": "Users retrieved successfully",
    "data": [UserData(_id=user.id, username=user.username, email=user.email) for user in users],
  }

@router.get("/me", response_description="User retrieved", response_model=Response)
async def get_user(token: dependencies=Depends(token_listener)):
  user = await get_current_user(token)
  if not user:
    raise HTTPException(
      status_code=404, 
      detail={
        "status_code": 404,
        "description": "Users not found",
        "response_type": "error",
        "data": None,
      }
    )
  return {
    "status_code": 200,
    "response_type": "success",
    "description": "User retrieved successfully",
    "data": user,
  }

# @router.get("/{id}", response_description="User retrieved", response_model=Response)
# async def get_user(id: PydanticObjectId):
#   user = await get_user_by_id(id)
#   if user:
#     return {
#       "status_code": 200,
#       "response_type": "success",
#       "description": "User retrieved successfully",
#       "data": user,
#     }
#   return {
#     "status_code": 404,
#     "response_type": "error",
#     "description": "User not found",
#     "data": None,
#   }

@router.put("/{id}", response_description="User data updated", response_model=Response)
async def update_user(id: PydanticObjectId, user: UpdateUser = Body(...) ):
  if user.password:
    user.password = hash_helper.hash(user.password)
  updated_user = await update_users_data(id, user.dict())
  if updated_user:
    return {
      "status_code": 200,
      "response_type": "success",
      "description": "User data and password updated successfully" if user.password else "User data updated successfully",
      "data": UserData(id=updated_user.id, username=updated_user.username, email=updated_user.email),
    }
  return {
    "status_code": 404,
    "response_type": "error",
    "description": "User not found",
    "data": None,
  }

# TODO delete berdasarkan token
@router.delete("/{id}", response_description="User data deleted", response_model=Response)
async def delete_user(id: PydanticObjectId):
  deleted_user = await delete_users(id)
  if deleted_user:
    return {
      "status_code": 200,
      "response_type": "success",
      "description": "User data deleted successfully",
      "data": None,
    }
  return {
    "status_code": 404,
    "response_type": "error",
    "description": "User not found",
    "data": None,
  }