# Python Control Flows

*THIS LESSON WILL COVER CONTROL FLOW*

## If statements, elif, and else statements
### for loops and while loops

## While loops
- While loops keep going until a certain condition is met
- Though not regularlyl used in the industry, it can be used for monitoring
- We have the key-words ```break``` and  ```continue``` to dictate what happens to the flow of the loop.

### Let's create a whioe loop
- break and continue are key words that we can use to control the flow of our program
- Syntax: While variable_name condition value:

`number = 0
while number < 10:
print(f"it's working -> {number}")
if number == 4:
break
number += 1`

### take user input with while loop

`user_prompt = True`

`while user_prompt:
    age = input(("Please enter your age? "))`
    
***Note this user inout is within our while therefore it will prompt the user until we get desired input***

***isdigit() is a python library method used to check if the input is all digits***

 `if age.isdigit() and int(age) < 117:`
 
        user_prompt = False
    else:
        print("Please provide age in digits")
