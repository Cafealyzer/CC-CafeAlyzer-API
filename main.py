from fastapi import Depends, FastAPI
from routers import maps
from routers import auth
from routers import user
from config.config import initiate_datebase
from auth.jwt_bearer import JWTBearer

app = FastAPI()

token_listener = JWTBearer()

@app.on_event("startup")
async def startup():
  await initiate_datebase()

@app.get("/")
async def root():
  return {"Welcome": "Cafe Analyzer API"}

app.include_router(auth.router, tags=["Authentication"])
app.include_router(maps.router, tags=["Maps"], prefix="/maps", dependencies=[Depends(token_listener)])
app.include_router(user.router, tags=["Users"], prefix="/users", dependencies=[Depends(token_listener)])