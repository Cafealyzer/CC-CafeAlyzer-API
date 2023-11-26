import os
import httpx
import subprocess
from typing import Annotated
from dotenv import load_dotenv
from fastapi import APIRouter, Query, Path
from fastapi.responses import Response

load_dotenv()
MAPS_API_KEY = os.getenv("MAPS_API_KEY")

router = APIRouter()

# TODO buatkan endpoint next_page
# TODO rapikan semua nya
@router.get("/nearby-search", tags=["Maps"])
async def nearby_search(
  keyword: Annotated[str, Query(
    title="Keyword",
    description="The text string on which to search for example: 'restaurant' or '123 Main Street'",
    example="cafe",
    min_length=3
  )],
  location: Annotated[str, Query(
    title="Location",
    description="The point around which to retrieve place information. This must be specified as latitude,longitude.",
    example="-1.2490478412943036, 116.86692126759571"
  )],
  radius: Annotated[int, Query(
    title="Radius",
    description="Defines the distance (in meters) within which to return place results.",
    example="1500"
  )],
  type: Annotated[str, Query(
    title="Type",
    description="Restricts the results to places matching the specified type.",
    example="cafe"
  )],
):
  url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
  params = {
    "keyword": keyword,
    "location": location,
    "radius": radius,
    "type": type,
    "rankby": "prominence",
    "fields": "formatted_address,name,rating,opening_hours,geometry,reviews",
    "key" : MAPS_API_KEY
  }
  
  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(url, params=params)
    return response.json()
  except subprocess.CalledProcessError as e:
      print(f"Error: {e}")

@router.get("/find-place")
async def find_place(
  input: Annotated[
	str,
	Query(
		title="Input",
    	description="The text string on which to search, for example: 'restaurant' or '123 Main Street'. ",
		example="fusion cafe"
	)],
  location: Annotated[
    str, 
    Query(
		title="Location",
    	description="The point around which to retrieve place information. This must be specified as latitude,longitude.",
		example="-1.2490478412943036, 116.86692126759571"
	)],
  radius: Annotated[
    str,
    Query(
       title="Radius",
       description="Prefer results in a specified area, by specifying either a radius plus lat/lng, or two lat/lng pairs representing the points of a rectangle. example: radius@lat,lng",
       example="2000"
	)]
):
  url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
  params = {
    "fields": "formatted_address,name,rating,geometry,place_id",
    "input": input,
    "inputtype": "textquery",
    "locationbias": "circle:"+radius+"@"+location,
    "key": MAPS_API_KEY
  }

  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(url, params=params)
    return response.json()
  except subprocess.CalledProcessError as e:
      print(f"Error: {e}")
      
@router.get("/place-detail/{place_id}", tags=["Maps"])
async def place_detail(place_id: Annotated[
  str,
  Path(
    title="place_id",
    description="A textual identifier that uniquely identifies a place, returned from a Place Search.",
    example="ChIJS-Ab2GZG8S0RTbY0FHmsYa8"
  )
]):
  url = "https://maps.googleapis.com/maps/api/place/details/json"
  params = {
    "fields": "place_id,rating,reviews,user_ratings_total,url,types,formatted_address,formatted_phone_number,business_status,photos",
    "place_id": place_id,
    "key": MAPS_API_KEY
  }

  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(url, params=params)
    return response.json()
  except subprocess.CalledProcessError as e:
      print(f"Error: {e}")
    
@router.get(
  "/place-photo", 
  tags=["Maps"],
)
async def place_photo(
  photo_reference: Annotated[
    str,
    Query(
      title="photo_reference",
      description="A string identifier that uniquely identifies a photo. Photo references are returned from either a Place Search or Place Details request.",
     	example="AcJnMuEu3-03PdQbBqrsrKK4U5gaLiUUxmEYGQFgiFYdZP74g8-VLwVjuc4KnxJETc_CUNRhO0w4q1UAY5_jqTAjEf5ou2VnN9Q7WaO6llrR82reafCWICON7SA26xpRPxIwNvZCSO-qWIjFK9Zq7F7hzTAzrKQ3zQwdIiDTls_K-wnRDlRL"
  )],
  max_width: 
    int = Query(
      title="Max Width",
      example=1280
	),
  max_height: 
    int | None = Query(
      default=None,
    	title="Max Height",
      example=400
		)
):
  url = "https://maps.googleapis.com/maps/api/place/photo"
  params = {
    "photo_reference": photo_reference,
    "maxwidth": max_width,
    "maxheight": max_height,
    "key": MAPS_API_KEY
  }

  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(url, params=params, follow_redirects=True)
      return Response(response.content, media_type="image/png")
  except subprocess.CalledProcessError as e:
      print(f"Error: {e}")