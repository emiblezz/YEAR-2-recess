#add here code to save customer into customer table
import electricity_bill


account_no=input("Enter Account Number:\n")
phone_no=input("Enter Phone Number :\n")
status=input("What is the status of your power (off/on) :\n")
location_coordinates=input("What are your Location coordinates :\n")
name = input("Enter User Name:\n")

customer1=electricity_bill.Customer(name,account_no,status,location_coordinates,phone_no)
print(customer1.add_customer())