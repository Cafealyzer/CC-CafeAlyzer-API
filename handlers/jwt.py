import time
import jwt 
from typing import Dict
from config.config import Settings
from jose import jwt
from config.config import Settings

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