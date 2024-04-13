from peewee import *
import datetime
db = SqliteDatabase('Orders.sqlite')

clmnsBooking = ('id', 'table_ID', 'guest_ID', 'bookedDate', 'bookedTime', 'guestsCount')
clmnsTables = ('id', 'guestCountMax', 'vipStatus')
clmnsGuests = ('id', 'name', 'surname', 'phone', 'email')


class Booking(Model):
    id = PrimaryKeyField(null=False)
    table_ID = BigIntegerField(null=False)
    guest_ID = BigIntegerField(null=False)
    #bookedDateTime = DateTimeField(default=datetime.datetime.now())
    bookedDate = DateTimeField(default=datetime.datetime.now().date())
    bookedTime = DateTimeField(default=datetime.datetime.now().time())
    guestsCount = BigIntegerField(null=False)

    class Meta:
        database = db
        order_by = ('id')

class Tables(Model):
    id = PrimaryKeyField(null=False)
    guestCountMax = BigIntegerField(null=False)
    vipStatus = BooleanField(null=False)

    class Meta:
        database = db
        order_by = ('id')

class Guests(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    surname = CharField(null=False)
    phone = CharField(null=False)
    email = CharField(null=False)

    class Meta:
        database = db
        order_by = ('id')

