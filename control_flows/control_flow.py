# control flow
# if statements
# Syntax: if then condition

# age = 15
#
# if age > 15:
#     print("Thank you, you are old enough to watch the movie")
#
# elif age <= 15:
#     print("Sorry you are too young.... try again when you grow up")
#
# else:
#     print("OOPs sorry something went wrong, try again later")


# create a program using control flow with if, elif and else
# using operators == >=
# check age restrictions before selling the ticket
# 18, 15, U, 12, PG

age = 19

if age < 3:
    print("Way too young, you should watch a film rated U")
elif age <= 11:
    print("You are in need of Parental Guidance (PG)")
elif age <= 14:
    print("You're not quite there yet. Watch TV 12")
elif age < 18:
    print("Almost old enough to watch 18, but still too young")
else:
    print("You can watch any film you like")

