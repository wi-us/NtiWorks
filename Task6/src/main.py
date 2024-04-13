import database as data
from peewee import *
from interface import root

if data.db.is_closed() == False:
    data.db.connect()

cursor = data.db.cursor()


data.Guests.create_table()
data.Booking.create_table()
data.Tables.create_table()


root.mainloop()