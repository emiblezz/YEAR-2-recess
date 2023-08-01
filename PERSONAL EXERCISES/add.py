#insert into billing table and capture into billing
import sqlite3
connection = sqlite3.connect('bills/bills.db')
cursor= connection.cursor()

def add_prices(self):
  if cursor.execute("INSERT INTO User(flate_units, flat_unit_rate,other_unit_rate, service_fee) values(?,?,?,?)",(self.f, self.tax_rate,self.pc, self.service_fee) values)):
    connection.commit():
    return f"{self.ElectricityBill} complete process"
  else:
    return f"{self.ElectricityBill} please try again"
