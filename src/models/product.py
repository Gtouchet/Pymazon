import peewee as pw

from src.models.category import Category
from src.models.tag import Tag

db = pw.SqliteDatabase('pymazon.db', pragmas={'foreign_keys': 1})

class Product(pw.Model):

    id = pw.AutoField()
    name = pw.CharField()
    price = pw.FloatField()
    description = pw.CharField()
    category = pw.ForeignKeyField(Category, backref="products")
    tag = pw.ManyToManyField(Tag, backref="products")

    class Meta:
        database = db
