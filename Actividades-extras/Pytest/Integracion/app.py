# app.py
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DATABASE = "test.db"

class Item(BaseModel):
    id: int

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY
        )
    """)
    return conn

@app.post("/items/", status_code=201)
def create_item(item: Item):
    db = get_db()
    try:
        db.execute("INSERT INTO items (id) VALUES (?)", (item.id,))
        db.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Item ya existe")
    finally:
        db.close()
    return {"id": item.id}

@app.get("/items/")
def list_items():
    db = get_db()
    cursor = db.execute("SELECT id FROM items ORDER BY id")
    items = [row[0] for row in cursor]
    db.close()
    return items
