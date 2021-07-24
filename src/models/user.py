import datetime
import peewee as pw


db = pw.SqliteDatabase('pymazon.db', pragmas={'foreign_keys': 1})

class User(pw.Model):
    id = pw.AutoField()
    firstName = pw.CharField()
    lastName = pw.CharField()
    address = pw.CharField(default="")
    mailAddress = pw.CharField()
    createdDate = pw.DateTimeField(default=datetime.datetime.now())
    class Meta:
        database = db
