import time
import jwt 
from typing import Dict
from config.config import Settings
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from config.config import Settings
from models.user import User

secret_key = Settings().SECRET_KEY

def token_response(token: str):
  return {
    "type": "bearer",
    "access_token": token
  }

def sign_jwt(username: str) -> Dict[str, str]:
  payload = {
    "username": username,
    "expires": time.time() + 2_628_000
  }
  token = jwt.encode(payload, secret_key, algorithm="HS256")
  return token_response(token)

def decode_jwt(token: str) -> dict:
  decoded_token = jwt.decode(token.encode(), secret_key, algorithms=["HS256"])
  return decoded_token if decoded_token["expires"] >= time.time() else {}

# TODO rapikan lagi ni method
async def get_current_user(token: str):
  credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Could not validate credentials",
      headers={"Authenticate": "Bearer"},
  )
  try:
      payload = decode_jwt(token)
      username: str = payload['username']
      if username is None:
          raise credentials_exception
      user = await User.find_one(User.username == username)
      if user is None:
          raise credentials_exception
      return user
  except JWTError:
      raise credentials_exception