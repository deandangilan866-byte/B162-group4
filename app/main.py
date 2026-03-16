from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from app.auth import verify_api_key
from app.limiter import limiter
from app.buyer_service import get_buyer_accounts

app = FastAPI(title="Ad Exchange Buyer API Integration")

app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc):

    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests. Please try again later."},
    )


@app.get("/")
def home():

    return {
        "message": "Ad Exchange Buyer API Service Running"
    }


@app.get("/buyers")
@limiter.limit("5/minute")
def buyers(request: Request, api_key: str = Depends(verify_api_key)):

    data = get_buyer_accounts()

    return {
        "buyers_data": data
    }