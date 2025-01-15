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


# @app.post("/post-reel/")
# async def post_reel(reel: Reel):
#     instagram_access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
#     if not instagram_access_token:
#         raise HTTPException(
#             status_code=500, detail="Instagram access token not found")

#     # Generate description
#     description_response = await generate_description(reel)
#     caption = description_response["description"]

#     # Post reel to Instagram (pseudo-code, replace with actual API call)
#     response = requests.post(
#         "https://graph.instagram.com/v1.0/me/media",
#         params={
#             "access_token": instagram_access_token,
#             "video_url": reel.video_url,
#             "caption": caption
#         }
#     )

#     if response.status_code != 200:
#         raise HTTPException(
#             status_code=response.status_code, detail=response.text)

#     return {"message": "Reel posted successfully"}


# uvicorn main:app --reload
