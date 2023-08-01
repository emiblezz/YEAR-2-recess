#insert date into pricing table
import electricity_bill
flat_units=input("Enter the number of flat unites: ")
flat_unit_rate=input("Enter the flat unit rate: ")
other_unit_rate=input("Enter the preceedin unit rate: ")
service_fee=input("Enter the amount of service fee: ")

details=electricity_bill.Pricing(flat_units,flat_unit_rate,other_unit_rate,service_fee)
print(details.add_prices())