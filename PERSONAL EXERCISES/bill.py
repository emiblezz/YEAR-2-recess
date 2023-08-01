import electricity_bill
import bill1
#calculate bills
customer_id=input("Enter customer id number: ")
previous_reading=input("Enter the Previous meter readings: ")
current_reading=input("Enter the current meter readings: ")
balance_bf=input("Enter the balance brought forward: ")


bill1=electricity_bill.Billing(customer_id,previous_reading,current_reading,balance_bf)
print(bill1.add_bills())

