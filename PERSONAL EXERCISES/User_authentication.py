def user_details():

    output = (f"Welcome :) {name},\n " + "login successful ")
    return output

name = input("Enter Username Please: \n")
password = input("Enter password: \n")


my_details = user_details()
print(my_details)

