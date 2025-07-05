
from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    role: str  # 'sender', 'receiver', 'sme'
    name: str

class CardRequest(BaseModel):
    card_number: str
    receiver_id: str

class TransferRequest(BaseModel):
    sender_id: str
    card_number: str
