from fastapi import FastAPI
from routers import maps

app = FastAPI()


@app.get("/")
async def root():
  return {"Welcome": "Cafe Analyzer API"}

app.include_router(maps.router)