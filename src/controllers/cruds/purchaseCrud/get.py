from src.models.purchase import Purchase

def getPurchase(id):
    return Purchase.select() if id == 0 else Purchase.get_by_id(id)
