from urllib import response
from beanie import PydanticObjectId
from fastapi import APIRouter, Body, Depends, HTTPException, dependencies
from auth.jwt_bearer import JWTBearer
from handlers.history import *
from schema.response import *
from models.history import History

router = APIRouter()

token_listener = JWTBearer()

@router.get("/me", response_description="User history retrieved", response_model=Response)
async def get_user_history(token: dependencies=Depends(token_listener)):
  histories = await get_all_user_histories(token)
  return {
    "status_code": 200,
    "response_type": "success",
    "description": "Histories retrieved successfully",
    "data": histories,
  }

@router.post("/", response_description="History created", response_model=Response)
async def create_history(history: History = Body(...)):
  history = await create_user_history(history)
  return {
    "status_code": 201,
    "response_type": "success",
    "description": "History created successfully",
    "data": history,
  }

@router.delete("/{id}", response_description="History deleted", response_model=ResponseDeleteHistory)
async def delete_history(id: PydanticObjectId):
  validation = await validation_history(id)
  if not validation:
    raise HTTPException(
      status_code=404, 
      detail={
        "status_code": 404,
        "description": "History not found",
        "response_type": "error",
        "data": None,
      }
    )
  await delete_user_history(id)
  return {
    "status_code": 200,
    "response_type": "success",
    "description": "History deleted successfully",
  }