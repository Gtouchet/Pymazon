from src.models.purchase import Purchase


def countAllPurchase():

    return Purchase.select().count()
