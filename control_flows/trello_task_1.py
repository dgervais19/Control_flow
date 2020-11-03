# Calculating the year of birth

from datetime import date  # importing date from the library datetime

current_date = date.today().year

age = 30
name = "Bob"
year_of_birth = current_date - age

print(f"OMG {name}, you are {age} years old and was born in {year_of_birth}")









