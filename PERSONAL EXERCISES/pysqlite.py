import sqlite3
#create database
connection = sqlite3.connect('store_transaction.db')
cursor= connection.cursor()
#create stores table

sql1="""CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""
cursor.execute(sql1)
#create purchase table
sql2="""CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER,total_amount FLOAT, FORIEGN KEY(store_id) REFERENCE stores(store_id))"""

cursor.execute(sql2)

#add stores

cursor.execute("INSERT INTO stores VALUE(21,'Kenya,KE')")
cursor.execute("INSERT INTO stores VALUE(95,'Kenya,KE')")
cursor.execute("INSERT INTO stores VALUE(64,'Tanzania,TZ')")
#add to purchase

cursor.execute("INSERT INTO stores VALUES(54,21,15.49)")
cursor.execute("INSERT INTO stores VALUES(23,64,21.12)")
#add to age