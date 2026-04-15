import typer
import json
import os

app = typer.Typer()
DB_FILE = "data.jsonl"

@app.command()
def append(payload: str):
   
    try:
        json_data = json.loads(payload)
        
        with open(DB_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(json_data) + "\n")
        
        print(f"Successfully added payload to {DB_FILE}")
    except json.JSONDecodeError:
        print("Error: The provided string is not a valid JSON.")

@app.command()
def retrieve():
    if not os.path.exists(DB_FILE):
        print("No data stored yet.")
        return

    with open(DB_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        last_10 = [json.loads(line.strip()) for line in lines[-10:]]
        
        print(f"Last {len(last_10)} entries:")
        for i, entry in enumerate(last_10, 1):
            print(f"{i}. {entry}")

if __name__ == "__main__":
    app()