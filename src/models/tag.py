import peewee as pw

db = pw.SqliteDatabase('my_app.db', pragmas={'foreign_keys': 1})

class Tag(pw.Model):
    id = pw.AutoField()
    name = pw.CharField()

    class Meta:
        database = db
