import datetime
import random
from datetime import datetime as datetime1

from faker import Faker

from src.controllers.cruds.productCrud.get import getProduct
from src.controllers.cruds.purchaseCrud.create import createPurchase
from src.controllers.cruds.userCrud.get import getUser
from src.models.product import Product
from src.models.purchase import Purchase


class GenerateDataPurchase:

    def __init__(self):
        self.fake = Faker('fr_FR')

    def generateData(self, nbUser, nbProduct, nbPurchase):
        for i in range(nbPurchase):
            purchase = Purchase()
            product = getProduct(random.randint(1, nbProduct))
            user = getUser(random.randint(1, nbUser))
            purchase.product = product.id
            purchase.user = user.id

            purchase.name = str(i) + "--" + purchase.product.name
            purchase.deliveryAddress = self.fake.address()

            purchase.purchaseDate = datetime1.now() - datetime.timedelta(seconds=random.randint(1, 157248000))

            if purchase.purchaseDate.now() < datetime1.now() - datetime.timedelta(seconds=60*60*12):
                purchase.status = "PENDING"

            elif purchase.purchaseDate.now() < datetime1.now() - datetime.timedelta(seconds=60*60*24*7):
                purchase.status = "SEND"
                purchase.sendingDate = purchase.purchaseDate + datetime.timedelta(seconds=random.randint(1, 60*60*24*7))

            else:
                purchase.status = "RECEIVED"
                purchase.sendingDate = purchase.purchaseDate + datetime.timedelta(seconds=random.randint(1, 60*60*24*7))
                purchase.receptionDate = purchase.sendingDate + datetime.timedelta(seconds=random.randint(1, 60*60*24*22))
            createPurchase(purchase)