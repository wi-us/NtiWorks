from peewee import *
import datetime

db = SqliteDatabase('Orders2.sqlite')
db.connect()

EMPTY = "NoData"
ID = "id"

class BaseModel(Model):
    class Meta:
        database = db

class Tables(BaseModel):
    guestCountMax = BigIntegerField(null=False)
    vipStatus = BooleanField(null=False)

    @classmethod
    def createTable(cls, *args):
        val = args[0]
        return cls.create(guestCountMax=val[1], vipStatus=val[2])

    @classmethod
    def deleteTable(cls, table_id):
        query = cls.delete().where(cls.id == table_id)
        query = Booking.delete().where(Booking.guest == cls)
        query.execute()

    @classmethod
    def getAllTables(cls):
        if cls.select().count() == 0:
            return EMPTY
        else:
            _arr = []
            for val in cls.select():
                _arr.append([val.id, val.guestCountMax, val.vipStatus])
            return _arr
    
    @classmethod
    def getValyeById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            if value == ID:
                return cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()[0]
            else:
                return cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            
    @classmethod
    def updateTable(cls, *args):
        val = args[0]
        query = cls.update(guestCountMax=val[1], vipStatus=val[2]).where(cls.id == val[0])
        query.execute()

class Guests(BaseModel):
    name = CharField(null=False)
    surname = CharField(null=False)
    phone = CharField(null=False)
    email = CharField(null=False)

    @classmethod
    def createTable(cls, *args):
        val = args[0]
        return cls.create(name=val[1], surname=val[2], phone=val[3], email=val[4])

    @classmethod
    def deleteTable(cls, table_id):
        query = cls.delete().where(cls.id == table_id)
        query = Booking.delete().where(Booking.guest == cls)
        
        query.execute()

    @classmethod
    def getAllTables(cls):
        if cls.select().count() == 0:
            return EMPTY
        else:
            _arr = []
            for val in cls.select():

                    _arr.append([val.id, val.name, val.surname, val.phone, val.email])

            return _arr
    
    @classmethod
    def getValyeById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            if value == ID:
                return cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()[0]
            else:
                return cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            
    @classmethod
    def updateTable(cls, *args):
        val = args[0]
        query = cls.update(name=val[1], surname=val[2], phone=val[3], email=val[4]).where(cls.id == val[0])
        query.execute()

class Booking(BaseModel):
    table = ForeignKeyField(Tables, backref='bookings', null=True)
    guest = ForeignKeyField(Guests, backref='bookings', null=True)
    bookedDate = DateTimeField(default=datetime.datetime.now().date())
    bookedTime = DateTimeField(default=datetime.datetime.now().time())
    guestsCount = BigIntegerField(null=False)

    @classmethod
    def createTable(cls, *args):
        val = args[0]
        table_ID_1 = Tables.get(Tables.id == val[1])
        guest_ID_1 = Guests.get(Guests.id == val[2])
        
        return cls.create(table=table_ID_1, guest=guest_ID_1, bookedDate=val[3], bookedTime=val[4], guestsCount=val[5])

    @classmethod
    def deleteTable(cls, table_id):
        cls.delete().where(cls.id == table_id)
        query = cls.delete()
        query.execute()

    @classmethod
    def getAllTables(cls):
        if cls.select().count() == 0:
            return EMPTY
        else:
            _arr = []
            for val in cls.select():
                    try:
                        _arr.append([val.id, val.table, val.guest, val.bookedDate, val.bookedTime, val.guestsCount])
                    except:
                        cls.deleteTable(val.id)
            return _arr
    
    @classmethod
    def getValyeById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            if value == ID:
                return cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()[0]
            else:
                return cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            
    @classmethod
    def updateTable(cls, *args):
        val = args[0]
        table = Tables.get(Tables.id == val[1])
        guests = Guests.get(Guests.id == val[2])
        query = cls.update(table=table, guest=guests, bookedDate=val[3], bookedTime=val[4], guestsCount=val[5]).where(cls.id == val[0])
        query.execute()

