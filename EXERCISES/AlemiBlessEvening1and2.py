# Tuples.....................................................................................................................................
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# Output:
# Tuple: (1, 2, 3)


# Strings.....................................................................................................................................
my_string = "Hello, World!"
print("String:", my_string)

# Output:
# String: Hello, World!


# Sets.....................................................................................................................................
my_set = {1, 2, 3}
print("Set:", my_set)

# Output:
# Set: {1, 2, 3}


# Lists.....................................................................................................................................
my_list = [4, 5, 6]
print("List:", my_list)

# Output:
# List: [4, 5, 6]


# Dictionaries..............................................................................................................................
my_dict = {"name": "John", "age": 30}
print("Dictionary:", my_dict)

# Output:
# Dictionary: {'name': 'John', 'age': 30}


# Format.....................................................................................................................................
formatted_string = "My name is {} and I'm {} years old.".format(my_dict["name"], my_dict["age"])
print("Formatted String:", formatted_string)

# Output:
# Formatted String: My name is John and I'm 30 years old.


# Casting.....................................................................................................................................
num_str = "10"
num_int = int(num_str)
print("Casting:", num_int)

# Output:
# Casting: 10


# Boolean.....................................................................................................................................
is_true = True
is_false = False
print("Boolean:", is_true, is_false)

# Output:
# Boolean: True False

#Exercise One.................................................................................................................................

my_dict = {"a": 1, "b": 2, "c": 3}

# Get a list of all values in the dictionary
values_list = list(my_dict.values())
print("Values:", values_list)

# Output:
# Values: [1, 2, 3]

#Exercise TWO...............................................................................................................................

my_dict = {"a": 1, "b": 2, "c": 3}

# Check if a key exists in the dictionary....................................................................................................
if "b" in my_dict:
    print("Key 'b' exists in the dictionary")
else:
    print("Key 'b' does not exist in the dictionary")

# Output:
# Key 'b' exists in the dictionary

#Exercise THREE...............................................................................................................................

my_dict = {"a": 1, "b": 2, "c": 3}

# Change the value of a specific key
my_dict["b"] = 4
print("Updated Dictionary:", my_dict)

# Output:
# Updated Dictionary: {'a': 1, 'b': 4, 'c': 3}

#Exercise FOUR..........................................................................................................................

my_dict = {"a": 1, "b": 2}
new_dict = {"c": 3, "d": 4}

# Update the original dictionary with new key-value pairs
my_dict.update(new_dict)
print("Updated Dictionary:", my_dict)

# Output:
# Updated Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}



my_dict = {"a": 1, "b": 2}

# Add a new key-value pair to the dictionary............................................................................................
my_dict["c"] = 3
print("Updated Dictionary:", my_dict)

# Output:
# Updated Dictionary: {'a': 1, 'b': 2, 'c': 3}


my_dict = {"a": 1, "b": 2, "c": 3}

# Remove a specific key-value pair from the dictionary..................................................................................
del my_dict["b"]
print("Updated Dictionary:", my_dict)

# Output:
# Updated Dictionary: {'a': 1, 'c': 3}



my_dict = {"a": 1, "b": 2, "c": 3}

# Iterate over the dictionary.........................................................................................................
for key, value in my_dict.items():
    print(key, ":", value)

# Output:
# a : 1
# b : 2
# c : 3


person1 = {"name": "John", "age": 30}
person2 = {"name": "Alice", "age": 25}
person3 = {"name": "Bob", "age": 35}

# Create a nested dictionary......................................................................................................
nested_dict = {"person1": person1, "person2": person2, "person3": person3}
print("Nested Dictionary:", nested_dict)

# Output:
# Nested Dictionary: {'person1': {'name': 'John', '



# Exercise: Using Booleans in a Conditional Statement.............................................................................

# Boolean variable
is_raining = True

# if Conditional statement using the boolean variable.............................................................................
if is_raining:
    print("It's raining outside. Don't forget your umbrella!")
else:
    print("The weather is clear. Enjoy your day!")

# Output:
# It's raining outside. Don't forget your umbrella!


#while condition statement using boolean variable..................................................................................
# Initialize the boolean variable
is_running = True

# Loop continues as long as is_running is True
while is_running:
    user_input = input("Enter 'stop' to exit: ")
    if user_input.lower() == "stop":
        is_running = False
    else:
        print("Invalid input. Please try again.")

print("Program has stopped.")

# Example Output:

# Enter 'stop' to exit: continue
# Invalid input. Please try again.
# Enter 'stop' to exit: hello
# Invalid input. Please try again.
# Enter 'stop' to exit: Stop
# Program has stopped.
