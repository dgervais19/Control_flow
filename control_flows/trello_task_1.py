# Calculating the year of birth

from datetime import date  # importing date from the library datetime

current_date = date.today()
current_year = date.today().year
current_month = date.today().month
current_day = date.today().day

age = int(input("what is your age?")) # sets a value to the variable age
name = input("what is your name?")
bd_yet = input("Have you had your birthday this year? (Y/N)")

if bd_yet == "Y":
    year_of_birth = current_year - age
if bd_yet == "N":
    year_of_birth = current_year - (age+1)

print(f"OMG {name}, you are {age} years old and was born in {year_of_birth}")
# print(date.today())


# print("Please enter your date of birth")
# bd_year = int(input("Year: "))
# bd_month = int(input("Month(1-12): "))
# bd_day = int(input("Day: "))
#
# if bd_month < current_month and bd_day < current_day:
#     print("your birth month has already gone")
# elif bd_month == current_month and bd_day == current_day:
#     print("Today is your birthday! Happy Birthday !")
# else:
#     print("Your birthday hasn't come yet")










