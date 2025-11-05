from fastapi import APIRouter, Query, HTTPException
import os, requests
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/weather", tags=["Weather"])

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@router.get("/")
def get_weather(city: str = Query(..., description="City name")):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()
        
        if res.status_code != 200 or "main" not in data:
            raise HTTPException(status_code=404, detail="City not found or API error")

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
