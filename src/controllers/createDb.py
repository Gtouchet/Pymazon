import peewee as pw

from src.models.product import Product
from src.models.user import User

db = pw.SqliteDatabase('pymazon.db')


def createDb():
    db.create_tables([Product])
    db.create_tables([User])

    Product.create(name='Pizza', price=5000)
    Product.create(name='Love', price=150)
    Product.create(name='Nessie', price=3.5)

    User.create(name="Thibaud")

    db.close()
