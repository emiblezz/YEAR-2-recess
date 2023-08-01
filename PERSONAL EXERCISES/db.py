import sqlite3
connection = sqlite3.connect('bills/bills.db')
cursor= connection.cursor()

sql1 = """CREATE TABLE IF NOT EXISTS
Customer(id INTEGER PRIMARY KEY autoIncrement,name TEXT,account_no VARCHAR(15), location_coordinates VARCHAR(32), status TEXT,phone_no VARCHAR(15))"""
cursor.execute(sql1)

sql2 = """CREATE TABLE IF NOT EXISTS
Pricing(id INTEGER PRIMARY KEY autoIncrement,flat_units INTEGER, flat_unit_rate FLOAT,other_unit_rate FLOAT,vat_rate FLOAT, service_fee FLOAT)"""
cursor.execute(sql2)

sql3 = """CREATE TABLE IF NOT EXISTS
Billing(id INTEGER PRIMARY KEY autoIncrement,customer_id INTEGER,previous_reading FLOAT,current_reading FLOAT, balance_bf FLOAT)"""
cursor.execute(sql3)

#sql4="""ALTER TABLE Billing ADD COLUMN billings_total FLOAT"""
#cursor.execute(sql4)
#sql5="""UPDATE Billing  set billings_total=22297 where id=1"""
#cursor.execute(sql5)


connection.commit()

