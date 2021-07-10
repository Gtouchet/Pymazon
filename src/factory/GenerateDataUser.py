import datetime
import random
from datetime import datetime as datetime1

from src.controllers.cruds.userCrud.create import createUser
from src.models.user import User
from faker import Faker


class GenerateDataUser:

    def __init__(self):
        self.fake = Faker('fr_FR')
    
    def generateData(self, nbUser):
        for i in range(nbUser):
            user = User()
            user.name = self.fake.user_name()
            user.lastName = self.fake.first_name()
            user.firstName = self.fake.last_name()
            user.address = self.fake.address()
            user.mailAddress = self.fake.email()
            user.createdDate = datetime1.now() - datetime.timedelta(seconds=random.randint(2592000, 157248000))
            # min = 60*60*24*30, max = 60*60*24*7*52*5
            createUser(user)
