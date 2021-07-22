from src.services.logger import Logger


def createPurchase(purchase):
    Logger("CreatePurchase", {
        "subject": "Create of " + purchase.name,
    })
    purchase.save()