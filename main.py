from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from utils import generate_description

load_dotenv()

app = FastAPI()


class Reel(BaseModel):
    prompt: str


app = FastAPI()


@app.get('/')
def healthcheck():
    return {"Status": "Api is running successfully"}


@app.post("/generate-description/")
async def generate_reel_description(reel: Reel):
    try:
        description = generate_description(reel.prompt)
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# uvicorn main:app --reload
