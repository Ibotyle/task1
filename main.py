from fastapi import FastAPI
from data import User

app = FastAPI()

db = User(

    slackUsername="dede64", 
    backend=1, 
    age=29,
    bio="Hi, I am dede64."
)


@app.get("/")
async def fetch_users():
    return db