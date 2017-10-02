from peewee import *    #from peewee import all Module.
from datetime import date   #from datetime import data.
from data import Ball, db   #from data.py import (class Ball),db Module. 

if __name__=='__main__':    #Excute when it is a main script.
    db.connect()    #connect database.
    db.create_tables([Ball],safe=True)  #create database's table and use (class Ball)'s format.
    print("create") #print create.
    steven = Ball(name='steven', date=date(2017, 9, 30), speed='3m/s')  #create data that named steven and use (class BAll)'s format to store .
    steven.save()   # steven is stored in the database.
    goodhaha = Ball(name='goodhaha', date=date(2017, 10, 1), speed='2m/s')
    goodhaha.save()
    db.close()  #disconnect database.
    