from src.models.purchase import Purchase
from src.services.logger import Logger


def deletePurchase(purchase):
    Logger("DeletePurchase", {
        "subject": "Delete of Purchase : " + str(purchase.id),
    })
    Purchase.delete().where(Purchase.id == purchase.id).execute()

def deletePurchaseWithUserId(id):
    purchases = Purchase.select().where(Purchase.user_id == id).execute()

    for purchase in purchases:
        deletePurchase(purchase)

def deletePurchaseWithProductId(id):
    purchases = Purchase.select().where(Purchase.product_id == id).execute()

    for purchase in purchases:
        deletePurchase(purchase)

