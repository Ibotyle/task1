from fastapi import FastAPI
from data import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

db = User(

    slackUsername="dede64", 
    backend=1, 
    age=29,
    bio="Hi, I am dede64."
)


@app.get("/api")
async def fetch_users():
    return db
