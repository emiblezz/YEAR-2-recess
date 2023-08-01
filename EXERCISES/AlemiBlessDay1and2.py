#IF CONDITION.....................................................................................................................................
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# Output:
# x is greater than 5

#if , elif, else..................................................................................................................................

age = int(input("Enter your age: "))

if age < 18:
    print("You are young and restricted from accessing any content.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#try, except and finally..........................................................................................................................

try:
    num = 10 / 0  # Attempting to divide by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always execute.")
    
 #try, except and finally 2.....................................................................................................................
 
try:
    age = int(input("Enter your age: "))
    print("Your age:", age)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
   

# Output:
# Error: Division by zero is not allowed.
# This block will always execute.

#For loop........................................................................................................................................

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#while loop......................................................................................................................................

count = 0

while count < 5:
    print("Count:", count)
    count += 1

#nested loops.....................................................................................................................................

rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        print("({}, {})".format(i, j), end=" ")
    print()

# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)

#Exercise "Mental health survry"...................................................................................................................

mental_health_dict = {
    1: "Feeling great! Keep up the positive mindset.",
    2: "Doing well overall. Stay positive and take care.",
    3: "Feeling a bit stressed. Consider taking breaks and practicing self-care.",
    4: "Experiencing some anxiety. Take a moment to relax and engage in calming activities.",
    5: "Feeling okay but could be better. Seek support from friends or family.",
    6: "Having a rough day. It's important to take care of yourself and reach out for help if needed.",
    7: "Feeling down. Try engaging in activities you enjoy or talk to someone you trust.",
    8: "Struggling with negative emotions. Consider seeking professional support.",
    9: "Feeling very sad. Reach out to a mental health professional or a helpline for assistance.",
    10: "Experiencing severe distress. Please seek immediate help from a professional or contact emergency services."
}

# Prompting the student to input their mental health status
name=input("Please Enter your name : \n")
mental_health_input = int(input("On a scale of 1-10, how is your mental health? \n "))

# Checking if the input is within the valid range
if 1 <= mental_health_input <= 10:
    # Getting the corresponding condition or remedy from the mental health dictionary
    condition = mental_health_dict[mental_health_input]
    print(f"Dear {name} I know you are ", condition)
else:
    print(f"Invalid input {name}. Please enter a number between 1 and 10.")




