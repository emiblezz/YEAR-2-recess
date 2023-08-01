import sqlite3
connection = sqlite3.connect('bills/bills.db')
cursor= connection.cursor()

class Customer():
  def __init__(self, name,account_no,status,location_coordinates,phone_no):
    self.name=name
    self.account_no=account_no
    self.status=status
    self.location_coordinates=location_coordinates
    self.phone_no=phone_no
    
  def __str__(self):
    txt = f"Current reading:{self.c},Previous readings:{self.p},proceeding rate:{self.pc},Flate Rate:{self.c}"
    return txt
  
  def add_customer(self):
    if cursor.execute("INSERT INTO Customer(name,account_no,location_coordinates,status,phone_no) VALUES(?,?,?,?,?)",(self.name,self.account_no,self.location_coordinates,self.status,self.phone_no)):
      connection.commit()
      return f"{self.name} completed succeessfully"
    else:
      return f"{self.name} please try again"
class Pricing():
  def __init__(self,flat_units,flat_unit_rate,other_unit_rate,service_fee):
    self.flat_units = flat_units
    self.flat_unit_rate = flat_unit_rate
    self.other_unit_rate = other_unit_rate
    self.service_fee=service_fee
    
  def add_prices(self):
    if cursor.execute("INSERT INTO Pricing(flat_units,flat_unit_rate,other_unit_rate,service_fee) VALUES(?,?,?,?)",(self.flat_units,self.flat_unit_rate,self.other_unit_rate,self.service_fee)):
      connection.commit()
      return "details successfully added"
    else:
      return "please try the process again please"

class Billing():
  def __init__(self,customer_id,previous_reading,current_reading,balance_bf):
    self.customer_id=customer_id
    self.current_reading = current_reading
    self.previous_reading = previous_reading
    self.balance_bf=balance_bf
  def add_bills(self):
    if cursor.execute("INSERT INTO Billing(customer_id,previous_reading,current_reading,balance_bf) VALUES(?,?,?,?)",(self.customer_id,self.previous_reading,self.current_reading,self.balance_bf)):
      connection.commit() 
      return "the process has been completed successfully"
    else:
      return "please try again, process failed"

  def update_bill(self,billing_id,billings_total):
    if cursor.execute("UPDATE Billing SET billings_total=? WHERE id=?",(billings_total,billing_id)):
      result=f"success"
      connection.commit()
    else:
      result=f"error try again please"
    