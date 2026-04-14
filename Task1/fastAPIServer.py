from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
import json
import os

app = FastAPI()
FILE_NAME = "data_store.jsonl"


class UserActivity(BaseModel):
    user_id: int
    username: str
    action: str
    importance: int = Field(ge=1, le=5)
    is_admin: bool = False
    tags: List[str] = []
    timestamp: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.post("/add")
async def add_payload(activity: UserActivity):
    with open(FILE_NAME, "a") as f:
        f.write(activity.model_dump_json() + "\n")
    return {"status": "success", "added": activity}

@app.get("/last")
async def get_last_payloads():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    last_10 = [json.loads(line) for line in lines[-10:] if line.strip()]
    return last_10