import os       #import os Module. 
from peewee import *    #from peewee import all Module.
from datetime import date   #from datetime import date Module. 

fileName = 'data.db'    #named filename = data.db .

db = SqliteDatabase(fileName)   #create database. 

class Ball(Model):  #create (class Ball) and get Model from peewee.
    name = CharField()  #create CharField() called name.
    date = DateField()  #create DateField() called data.
    speed = CharField() #create CharField() called speed.
    class Meta: #meta get from model and use to named.
        database = db   #named database =db.
        

if __name__=='__main__':    #Excute when it is a main script.
    fileExist = os.path.isfile(fileName)    #if (b.bd) is exist.

    db.connect()    #connect database.     
    db.create_tables([Ball], safe=True) #create database's table and use (class Ball)'s format.
    if not fileExist:   #if data.db is not exist.
        print("create") #print create.
        steven = Ball(name='steven', date=date(2017, 9, 30), speed='3m/s')  #create data that named steven and use (class BAll)'s format to store .  
        steven.save()   # steven is stored in the database.
    else:   #if data.db is exist. 
        print("read")   #print read.
        for ball in Ball.select():  #retrieve the data from (class Ball).
            print(ball.name, ball.date, ball.speed) #print ball.name, ball.date, ball.speed
    db.close()  #disconnect database.
