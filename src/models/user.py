import peewee as pw

db = pw.SqliteDatabase('my_app.db', pragmas={'foreign_keys': 1})

class User(pw.Model):
    id = pw.AutoField()
    name = pw.CharField()
    firstName = pw.CharField()
    lastName = pw.CharField()
    address = pw.CharField()
    zipCode = pw.IntegerField()
    mailAddress = pw.CharField()

    class Meta:
        database = db
