# Project data representation 2020
# Blueberry harvest data by employee

# Import all required libraries
import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg


class BalticDao:
    db = ""

    def __init__(self):

        #Connect the MySQL Database
        self.db = mysql.connector.connect(host=cfg.mysql['host'],
                                          user=cfg.mysql['user'],
                                          password=cfg.mysql['password'],
                                          database=cfg.mysql['database'])
   
    def create(self, harvest):
        cursor = self.db.cursor()
        sql = "insert into harvest (id, employeeName, fieldSection, variety, quantity) values (%s,%s,%s,%s,%s)"
        values = [
            harvest['id'], harvest['employeeName'], harvest['fieldSection'], harvest['variety'], harvest['quantity']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid
