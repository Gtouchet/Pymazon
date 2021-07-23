from src.controllers.cruds.purchaseCrud.delete import deletePurchase
from src.models.purchase import Purchase


def deletePurchaseWithUserId(id):
    purchases = Purchase.select().where(Purchase.user_id == id).execute()

    for purchase in purchases:
        deletePurchase(purchase)