from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

CORRECT_ANSWER = 60  # 10 + 20 + 30

class Payload(BaseModel):
    email: str
    secret: str
    url: str
    answer: float

@app.post("/submit")
def submit(payload: Payload):
    if payload.answer == CORRECT_ANSWER:
        return {
            "correct": True,
            "url": None,
            "reason": None
        }
    return {
        "correct": False,
        "reason": "Wrong sum",
        "url": None
    }
