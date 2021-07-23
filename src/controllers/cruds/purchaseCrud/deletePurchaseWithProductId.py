from src.controllers.cruds.purchaseCrud.delete import deletePurchase
from src.models.purchase import Purchase


def deletePurchaseWithProductId(id):
    purchases = Purchase.select().where(Purchase.product_id == id).execute()

    for purchase in purchases:
        deletePurchase(purchase)