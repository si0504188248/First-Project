from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import sqlite3

DB_NAME = "DB_FILE.db"
HISTORY_LINES = 10
GENERAL_ERROR_CODE = 500

class User(BaseModel):
    user_id: int
    username: str

def db_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error:
        raise HTTPException(status_code=GENERAL_ERROR_CODE, detail="Database connection failed")

app = FastAPI()

@app.on_event("startup")
def setup_db():
    with db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS history 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,data TEXT NOT NULL)''')

@app.post("/add")
async def add_payload(user: List[User]):
    try:
        with db_connection() as conn:
            for u in user:
                conn.execute("INSERT INTO history (data) VALUES (?)", (u.model_dump_json(),))
            conn.commit()
            return {"status": "success", "added": user}
    except Exception as e:
        raise HTTPException(status_code=GENERAL_ERROR_CODE, detail=f"Failed to save data: {str(e)}")

@app.get("/history")
async def get_last_payloads():
    try:
        with db_connection() as conn:
            query = f"SELECT data FROM history ORDER BY id DESC LIMIT {HISTORY_LINES}"
            cursor = conn.execute(query)
            rows = cursor.fetchall()
            return [json.loads(row['data']) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve data")
