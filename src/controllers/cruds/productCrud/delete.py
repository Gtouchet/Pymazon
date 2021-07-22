from src.controllers.cruds.purchaseCrud.delete import deletePurchaseWithProductId
from src.models.product import Product
from src.services.logger import Logger


def deleteProduct(product):
    Logger("DeleteProduct", {
        "subject": "Delete of Product :" + product.name
    })
    Product.delete().where(Product.id == product.id).execute()


def deleteProductWithTagId(id):
    products = Product.select().where(Product.tag_id == id).execute()

    for product in products:
        deletePurchaseWithProductId(product.id)
        deleteProduct(product)
