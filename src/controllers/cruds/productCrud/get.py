from src.models.product import Product


def getProduct(id):
    if id == 0:
        return Product.select()
    else:
        return Product.get_by_id(id)
