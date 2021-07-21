from src.models.purchase import Purchase

def deletePurchase(id):
    Purchase.delete_by_id(id)