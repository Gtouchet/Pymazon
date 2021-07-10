from src.controllers.cruds.productCrud.countAll import countAllProduct
from src.controllers.cruds.productCrud.get import getProduct
from src.controllers.cruds.userCrud.countAll import countAllUser
from src.controllers.cruds.userCrud.get import getUser
from src.factory.GenerateDataCategory import GenerateDataCategory
from src.factory.GenerateDataProduct import GenerateDataProduct
from src.factory.GenerateDataPurchase import GenerateDataPurchase
from src.factory.GenerateDataTag import GenerateDataTag
from src.factory.GenerateDataUser import GenerateDataUser


class GenerateData:

    def __init__(self):
        self.generateDataUser = GenerateDataUser()
        self.generateDataCategory = GenerateDataCategory()
        self.generateDataTag = GenerateDataTag()
        self.generateDataProduct = GenerateDataProduct()
        self.generateDataPurchase = GenerateDataPurchase()

    def generateAllData(self, nbUser, nbProduct, nbPurchase):
        self.generateDataCategory.generateData()
        self.generateDataTag.generateData()
        self.generateDataUser.generateData(nbUser)
        self.generateDataProduct.generateData(nbProduct)
        self.generateDataPurchase.generateData(nbUser, nbProduct, nbPurchase)

    def generateNewPurchase(self, nbPurchase):
        self.generateDataPurchase.generateData(countAllUser(), countAllProduct(), nbPurchase)
