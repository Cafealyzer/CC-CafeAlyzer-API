from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
import models as models

class Settings(BaseSettings):
	DATABASE_URL: str
	SECRET_KEY: str
	MAPS_API_KEY: str
	VERSION_APP: str

	class Config:
		env_file = ".env"
		from_attributes = True

async def initiate_datebase():
	client = AsyncIOMotorClient(Settings().DATABASE_URL)
	try:
		client = AsyncIOMotorClient(Settings().DATABASE_URL)
		await init_beanie(
				database=client.get_default_database(), document_models=models.__all__
		)
	except Exception as e:
		print(f"Failed to connect to the database. Error: {e}")