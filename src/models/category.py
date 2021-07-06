import peewee as pw
db = pw.SqliteDatabase('pymazon.db', pragmas={'foreign_keys': 1})

class Category(pw.Model):
    id = pw.AutoField()
    name = pw.CharField()

    class Meta:
        database = db
