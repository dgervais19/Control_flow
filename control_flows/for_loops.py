# Loops For loop and While loop
# for loop is used to iterate through the data
# Syntax for variable_name in name_of_data_collection_variable

# creating a list called shopping list
shopping_list = ["eggs", "milk", "super malt"]
print(shopping_list)

# Creating a for loop that searches the list incrementally. Once it reaches "Milk" it prints that item
for items in shopping_list:
    if items == "milk":
        print(items)

# creating a dictionary called user_details
user_details = {
    "key": "value",
    "name": "Dono",
    "DOB": "12/02/1940",
    "course:": "Devops",
    "hobbies": ["basketball", "Piano", "Gym", "Socialising", "data types"]
}

# creating a for loop that seaeches each key in the dictionary and prints it
for keys in user_details:
    print(keys)

# # creating a for loop that searches each value in the dictionary and prints it
for values in user_details:
    print(values)

