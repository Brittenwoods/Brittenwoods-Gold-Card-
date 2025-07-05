
from fastapi import APIRouter, HTTPException
from app.models import User, CardRequest, TransferRequest
from app.logic import generate_pin, check_tree_limit

router = APIRouter()

users_db = {}
cards_db = {}

@router.post("/register_user/")
def register_user(user: User):
    if user.user_id in users_db:
        raise HTTPException(status_code=400, detail="User already exists.")
    users_db[user.user_id] = user
    return {"message": f"User {user.user_id} registered."}

@router.post("/request_card/")
def request_card(card: CardRequest):
    if card.card_number in cards_db:
        raise HTTPException(status_code=400, detail="Card already exists.")
    cards_db[card.card_number] = {
        "receiver_id": card.receiver_id,
        "is_active": False
    }
    return {"message": f"Card {card.card_number} issued."}

@router.post("/generate_pin/")
def get_pin(req: TransferRequest):
    pin, existing = generate_pin(req.sender_id, req.card_number)
    return {"pin": pin, "existing": existing}

@router.post("/check_tree/")
def tree_check(req: TransferRequest):
    user = users_db.get(req.sender_id)
    if not user:
        raise HTTPException(status_code=404, detail="Sender not found.")
    card = cards_db.get(req.card_number)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found.")
    receiver_id = card["receiver_id"]
    result, size = check_tree_limit(req.sender_id, receiver_id, user.role)
    if result == "LIMIT":
        raise HTTPException(status_code=403, detail="Transfer tree limit reached.")
    return {"status": result, "current_tree_size": size}
