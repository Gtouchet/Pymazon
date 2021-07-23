from src.models.product import Product
from src.models.purchase import Purchase


def getPurchaseWithCategoryId(id):
    products = Product.select().where(Product.tag.category_id == id).execute()

    purchases = []
    for product in products:
        purchases.append(Purchase.select().where(Purchase.product_id == product.id).execute())
    return purchases