# sql_connect_module

import copy
import threading
import os
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='Lm19orange@22', db='honeybird')

a = conn.cursor()

sql = 'SELECT * FROM user;'
a.execute(sql)
countrow = a.execute(sql)
print("Number of rows :",countrow)
data = a.fetchone()
print(data)



