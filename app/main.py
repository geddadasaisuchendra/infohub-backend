from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import weather, currency, quotes

app = FastAPI(title="InfoHub API", version="1.0")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(weather.router)
app.include_router(currency.router)
app.include_router(quotes.router)

@app.get("/")
def root():
    return {"message": "Welcome to InfoHub API"}
