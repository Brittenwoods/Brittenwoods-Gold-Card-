
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Brittenwoods Gold API"}

@app.get("/generate_pin/")
def generate_pin(card_number: str, sender_id: str):
    return {"pin": "3421", "card_number": card_number, "sender": sender_id}
