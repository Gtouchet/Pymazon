from src.models.purchase import Purchase
from src.services.logger import Logger


def deletePurchase(purchase):
    Logger("DeletePurchase", {
        "subject": "Delete of Purchase : " + str(purchase.id),
    })
    Purchase.delete().where(Purchase.id == purchase.id).execute()

