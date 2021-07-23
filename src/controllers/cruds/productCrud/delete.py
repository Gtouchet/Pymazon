from src.models.product import Product
from src.services.logger import Logger


def deleteProduct(product):
    Logger("DeleteProduct", {
        "subject": "Delete of Product :" + product.name
    })
    Product.delete().where(Product.id == product.id).execute()


