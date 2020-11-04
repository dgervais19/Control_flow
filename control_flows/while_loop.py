# Let's create a whioe loop
# break and continue are key words that we can use to control the flow of our program
# Syntax: While variable_name condition value:

# number = 0
#
# while number < 10:
#     print(f"it's working -> {number}")
#     if number == 4:
#         break
#     number += 1

# take user input with while loop

user_prompt = True

while user_prompt:
    age = input(("Please enter your age? "))
# Note this user inout is within our while therefore it will prompt the user until we get desired input

# isdigit() is a python library method used to check if the input is all digits
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide age in digits")