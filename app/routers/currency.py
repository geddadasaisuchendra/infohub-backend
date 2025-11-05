from fastapi import APIRouter, Query, HTTPException
import os, requests
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/convert", tags=["Currency Converter"])

API_KEY = os.getenv("EXCHANGERATE_API_KEY")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/INR"

@router.get("/")
def convert_currency(amount: float = Query(..., gt=0), to: str = Query(..., regex="^(USD|EUR)$")):
    try:
        res = requests.get(BASE_URL)
        data = res.json()

        if res.status_code != 200 or "conversion_rates" not in data:
            raise HTTPException(status_code=400, detail="API error")

        rate = data["conversion_rates"].get(to)
        converted = round(amount * rate, 2)

        return {
            "from": "INR",
            "to": to,
            "rate": rate,
            "converted": converted
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
