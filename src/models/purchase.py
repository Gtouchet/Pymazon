import peewee as pw

from src.models.product import Product
from src.models.user import User

db = pw.SqliteDatabase('pymazon.db', pragmas={'foreign_keys': 1})

class Purchase(pw.Model):
    id = pw.AutoField()
    name = pw.CharField()
    purchaseDate = pw.DateTimeField()
    sendingDate = pw.DateTimeField(null=True)
    receptionDate = pw.DateTimeField(null=True)
    status = pw.CharField()
    deliveryAddress = pw.CharField()
    user = pw.ForeignKeyField(User)
    product = pw.ForeignKeyField(Product)
    
    class Meta:
        database = db
