from fastapi import FastAPI
from routers import maps
from routers import auth

app = FastAPI()


@app.get("/")
async def root():
  return {"Welcome": "Cafe Analyzer API"}

app.include_router(maps.router)
app.include_router(auth.router)