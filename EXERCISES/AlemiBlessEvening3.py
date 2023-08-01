# Exercise 1 (Lists)
# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["John", "Alice", "Bob", "Emily", "Michael"]
print(names[1])

# 2. Write a python program to change the value of the first item to a new value
names[0] = "Peter"

# 3. Write a python program to add a sixth item to the list
names.append("Sarah")

# 4. Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")

# 5. Write a python program to remove the 4th item from the list
del names[3]

# 6. Use negative indexing to print the last item in your list
print(names[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
new_list = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Grapes"]
print(new_list[2:5])

# 8. Write a list of countries and make a copy of it.
countries = ["USA", "Canada", "Australia"]
countries_copy = countries.copy()

# 9. Write a python program to loop through the list of countries
for country in countries:
    print(country)

# 10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["Elephant", "Tiger", "Lion", "Giraffe"]
animals.sort()  # Ascending order
print(animals)
animals.sort(reverse=True)  # Descending order
print(animals)

# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
for animal in animals:
    if 'a' in animal.lower():
        print(animal)

# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Alice", "Bob"]
last_names = ["Doe", "Smith", "Johnson"]
full_names = first_names + last_names
print(full_names)


# Exercise 2 (Tuples)

# 1. Consider the tuple below;
x = ("samsung", "iphone", "tecno", "redmi")
# Write a python program to output your favorite phone brand.
favorite_brand = x[1]
print("My favorite phone brand is", favorite_brand)

# 2. Use negative indexing to print the 2nd last item in your tuple.
second_last_item = x[-2]
print("The second last item in the tuple is", second_last_item)

# 3. Using the phones list above, write a python program to update "iphone" to "itel"
updated_tuple = list(x)
updated_tuple[1] = "itel"
x = tuple(updated_tuple)
print("Updated tuple:", x)

# 4. Write a python program to add "Huawei" to your tuple.
x = x + ("Huawei",)
print("Updated tuple with Huawei:", x)

# 5. Write a python program to loop through the tuple above.
print("Looping through the tuple:")
for item in x:
    print(item)

# 6. Write a python program to remove/delete the first item in your tuple.
x = x[1:]
print("Tuple after removing the first item:", x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print("Uganda cities tuple:", uganda_cities)

# 8. Write a python program to unpack your tuple.
brand1, brand2, brand3, brand4, brand5 = x
print("Unpacked tuple:")
print("Brand 1:", brand1)
print("Brand 2:", brand2)
print("Brand 3:", brand3)
print("Brand 4:", brand4)
print("Brand 5:", brand5)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print("Cities at indexes 1, 2, and 3:", uganda_cities[1:4])

# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Jane", "David")
last_names = ("Doe", "Smith", "Johnson")
full_names = first_names + last_names
print("Joined tuples of first names and last names:", full_names)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print("Multiplied colors tuple:", multiplied_colors)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears in the tuple:", count_8)


# Exercise 3 (Sets)

# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print("Favorite beverages set:", beverages)

# 2. Use the correct method to add 2 more items to the beverages set.
beverages.add("water")
beverages.add("soda")
print("Updated beverages set:", beverages)

# 3. Given the set below;
mySet = {"oven", "kettle", "microwave", "refrigerator"}
# Check if "microwave" is present in the set.
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# 4. Write a python program to remove "kettle" from the set above.
mySet.remove("kettle")
print("Set after removing 'kettle':", mySet)

# 5. Write a python program to loop through the set above.
print("Looping through the set:")
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
set1 = {1, 2, 3, 4}
list1 = [5, 6]
set1.update(list1)
print("Updated set after adding elements from the list:", set1)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {20, 30, 40}
first_names = {"John", "Jane", "David"}
combined_set = ages.union(first_names)
print("Combined set of ages and first names:", combined_set)


# Exercise 4 (Strings)

# 1. Declare two variables, an integer and a string, and use the correct method to concatenate the two variables.
age = 25
name = "John"
concatenated_string = str(age) + " years old " + name
print("Concatenated string:", concatenated_string)

# 2. Consider the example below;
txt = " Hello, Uganda! "
# Output the string without spaces at the beginning, in the middle, and at the end.
stripped_string = txt.strip()
print("Stripped string:", stripped_string)

# 3. Write a python program to convert the value of 'txt' to uppercase.
uppercase_string = txt.upper()
print("Uppercase string:", uppercase_string)

# 4. Write a python program to replace the character 'U' with 'V' in the string above.
replaced_string = txt.replace("U", "V")
print("Replaced string:", replaced_string)

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd, and 4th position.
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print("Range of characters:", range_of_characters)

# 6. The piece of code below will give an error when output;
# x = "All "Data Scientists" are cool!" 
# Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print("Corrected string:", x)
