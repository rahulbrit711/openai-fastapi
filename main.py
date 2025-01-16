from fastapi import FastAPI, HTTPException, Security, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
from utils import generate_description
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader, APIKey
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = os.getenv("API_KEY_NAME")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=403, detail="Could not validate credentials")

app = FastAPI()

origins = [
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Reel(BaseModel):
    prompt: str


@app.get('/')
async def healthcheck(api_key: APIKey = Depends(get_api_key)):
    return {"Status": "Api is running successfully"}


@app.post("/generate-description/")
async def generate_reel_description(reel: Reel, api_key: APIKey = Depends(get_api_key)):
    try:
        description = generate_description(reel.prompt)
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# uvicorn main:app --reload
