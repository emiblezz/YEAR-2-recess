#calculate all bills for customers and display in tabulate format and save into Billing
import sqlite3
connection = sqlite3.connect('bills/bills.db')
cursor = connection.cursor()

from electricity_bill import Billing

from tabulate import tabulate
class ElectricityBill:
  def __init__(self, name, account_no, location_coordinates, status, phone_no, customer_id, current_reading, previous_reading, balance_bf,flat_units, flat_unit_rate, other_unit_rate, vat_rate, service_fee):
    self.name = name
    self.account_no = account_no
    self.location_coordinates = location_coordinates
    self.status = status
    self.phone_no = phone_no
    self.customer_id = customer_id
    self.current_reading = current_reading
    self.previous_reading = previous_reading
    self.balance_bf = balance_bf
    self.flat_units = flat_units
    self.flat_unit_rate = flat_unit_rate
    self.other_unit_rate = other_unit_rate
    self.vat_rate = vat_rate
    self.service_fee = service_fee
    
    
  def __str__(self):
    return f"current_reading: {self.current_reading}, previous_reading: {self.previous_reading}"
  def bill_calc(self):
    used_units = self.current_reading - self.previous_reading
     
    if used_units<=self.flat_units:
      total_bill = used_units*self.flat_unit_rate
      vat = (self.vat_rate/100) * total_bill
      total = total_bill + vat + self.service_fee + self.balance_bf
      return total
    else:
       flat_bill = self.flat_units * self.flat_unit_rate
       remaining_units = used_units - self.flat_units
       remaining_bill = remaining_units * self.other_unit_rate
       total_bill = flat_bill + remaining_bill
       vat = (self.vat_rate/100) * total_bill
       total = total_bill + vat + self.service_fee + self.balance_bf
       return total
    
cursor.execute("SELECT * FROM Pricing ORDER BY id desc LIMIT 1")
prices = cursor.fetchone()
flat_units = prices[1]
flat_unit_rate = prices[2]
other_unit_rate = prices[3]
vat_rate = prices[4]
service_fee = prices[5]
#print(prices)

cursor.execute("SELECT * FROM Customer")
results = cursor.fetchall()
v_results = []
for customer in results:
  customer_id = customer[0]
  customer_name = customer[1]
  account_no = customer[2]
  location_coordinates = customer[3]
  status = customer[4]
  phone_no = customer[5]
  cursor.execute("SELECT id, previous_reading, current_reading, balance_bf, billings_total FROM Billing WHERE customer_id = ? LIMIT 1", (customer_id,))
  readings = cursor.fetchone()
  billing_id=readings[0]
  previous_reading = readings[1]
  current_reading = readings[2]
  balance_bf = readings[3]
  billings_total = readings[4]

  customer_bill = ElectricityBill(customer_name, account_no, location_coordinates, status, phone_no, customer_id, current_reading, previous_reading, balance_bf,flat_units, flat_unit_rate, other_unit_rate, vat_rate, service_fee)

  #customer = list(customer)
  #v_results.append(customer)
  #print(customer_bill.bill_calc())
  bill_record=Billing(customer_id,current_reading,previous_reading,balance_bf)
  update_bill_record=bill_record.update_bill(billing_id,billings_total)
