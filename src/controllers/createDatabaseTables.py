import peewee as pw
from src.models.category import Category
from src.models.product import Product
from src.models.purchase import Purchase
from src.models.tag import Tag
from src.models.user import User
db = pw.SqliteDatabase('pymazon.db')

def createDatabaseTables():
    db.create_tables([Product])
    db.create_tables([User])
    db.create_tables([Category])
    db.create_tables([Purchase])
    db.create_tables([Tag])
    db.close()
