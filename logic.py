
pin_store = {}
transfer_tree = {}

def generate_pin(sender_id, card_number):
    key = (sender_id, card_number)
    if key in pin_store:
        return pin_store[key], True
    new_pin = str(1000 + hash(key) % 9000)
    pin_store[key] = new_pin
    return new_pin, False

def check_tree_limit(sender_id, receiver_id, role):
    tree = transfer_tree.get(sender_id, [])
    limit = 25 if role == "sme" else 15
    if receiver_id in tree:
        return "OK", len(tree)
    if len(tree) >= limit:
        return "LIMIT", len(tree)
    tree.append(receiver_id)
    transfer_tree[sender_id] = tree
    return "ADDED", len(tree)
