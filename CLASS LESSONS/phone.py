def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

number = [int(x) for x in input("Enter phone number: ").strip()]
if len(number) == 10:
  print(create_phone_number(number))
else:
  print("PLEASE CHECK YOUR NUMBER AGAIN! IT MAY BE LESS OR MORE THAN 10 DIGITS")
