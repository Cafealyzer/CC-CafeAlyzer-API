from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext
from models import user
from schema.response import ResponseLogin
from handlers.jwt import sign_jwt
from handlers.user import add_users
from models.user import User, UserLogin, UserData
from schema.response import Response

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@router.post("/register", response_description="User data added into the database", response_model=Response)
async def register_user(user: User = Body(...)):
    validation_username = await User.find_one({"username": user.username})
    validation_email = await User.find_one({"email": user.email})
    if validation_username:
      raise HTTPException(
        status_code=422,
        detail={
          "status_code": 422,
          "response_type": "error",
          "description": "Username already taken",
          "data": None,
        },
      )
    if validation_email:
      raise HTTPException(
        status_code=422,
        detail={
          "status_code": 422,
          "response_type": "error",
          "description": "Email already taken",
          "data": None,
        },
      )
    user.password = hash_helper.hash(user.password)
    new_user = await add_users(user)
    return {
      "status_code": 200,
      "response_type": "success",
      "description": "Register successful",
      "data": UserData(id=new_user.id, username=new_user.username, email=new_user.email),
    }

@router.post("/login", response_description="User logged in successfully", response_model=ResponseLogin)
async def login_user(user_credentials: UserLogin = Body(...)):
    user_exist = await User.find_one(User.username == user_credentials.username)
    if user_exist:
      password = hash_helper.verify(user_credentials.password, user_exist.password)
      if password:
        token = sign_jwt(user_credentials.username)
        return {
          "status_code": 200,
          "description": "Login Successfull",
          "token": token,
        }
      raise HTTPException(status_code=403, detail="Incorrect username or password")
    raise HTTPException(status_code=403, detail="Incorrect username or password")