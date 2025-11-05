from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(prefix="/quote", tags=["Motivational Quotes"])

@router.get("/")
def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        data = res.json()
        if isinstance(data, list) and data:
            return {
                "quote": data[0].get("q"),
                "author": data[0].get("a")
            }
        else:
            raise HTTPException(status_code=400, detail="Invalid API response")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
