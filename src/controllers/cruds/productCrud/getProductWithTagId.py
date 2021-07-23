from src.models.product import Product


def getProductWithTagId(id):
    return Product.select().where(Product.tag.id == id).execute()