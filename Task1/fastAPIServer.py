from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()
FILE_NAME = "DB_FILE.json"

class User(BaseModel):
    user_id: int
    username: str

@app.post("/add")
async def add_payload(user: List[User]):
    with open(FILE_NAME, "a") as f:
        for u in user:
            f.write(u.model_dump_json() + "\n")
    return {"status": "success", "added": user}

@app.get("/history")
async def get_last_payloads():
    if not os.path.exists(FILE_NAME):
        return "Didnt found"

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    last_10 = [json.loads(line) for line in lines[-10:] if line.strip()]
    return last_10


