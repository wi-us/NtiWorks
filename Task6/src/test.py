# Импортируем библиотеку, соответствующую типу нашей базы данных 
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
from peewee import *
from datetime import date
# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
db = SqliteDatabase('Chinook_Sqlite.sqlite')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'

if db.is_closed() == False:
    db.connect()

cursor = db.cursor()

Person.create_table()
Pet.create_table()

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save()  # cохраним Боба в базе данных

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

grandma.name = 'Grandma L.'
grandma.save()  # обновим запись grandma

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

herb_mittens.delete_instance()  # удачи, Варежк

herb_fido.owner = uncle_bob
herb_fido.save()
bob_fido = herb_fido  # переименуем переменную для лучшего соответствия суровой реальности
test = db.get_tables()
aws1 = db.get_columns(db.get_tables()[0])
db.create_tables([Person, Pet])
db.close()


