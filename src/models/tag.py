import peewee as pw

from src.models.category import Category

db = pw.SqliteDatabase('pymazon.db', pragmas={'foreign_keys': 1})


class Tag(pw.Model):
    id = pw.AutoField()
    name = pw.CharField()
    category = pw.ForeignKeyField(Category)


    class Meta:
        database = db
