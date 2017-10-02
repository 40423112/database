from peewee import *    #from peewee import all Module.
from data import Ball, db   #from data.py import (class Ball),db Module. 

if __name__=='__main__':    #Excute when it is a main script.
    db.connect()    #connect database.
    print("read")   #print create.
    db.create_tables([Ball], safe=True) #create database's table and use (class Ball)'s format.
    for ball in Ball.select():  #retrieve the data from (class Ball).
        print(ball.name, ball.date, ball.speed) #print ball.name, ball.date, ball.speed
    db.close()  #disconnect database.
