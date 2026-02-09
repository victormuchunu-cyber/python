# Python while loop
# Wile loop executes a block of code repeatedly as long as a certain condition is true. The synatx of a while loop is as follows.
"""
initialization of a variable
while keyword,
folowed by the condition/statement to be evaluated,
followed by a full colon(:),
code to be printed out,
increment/decrement
"""
number = 0
while number <  5:
    print("Hello Moses", number)
    number = number + 1

print('==============================')
# create a python program that prints the even numbers from 50 to 70 using while loop
number = 50
while number <= 70:
    if number % 2 == 0:
        print(number)
    number += 1

print('==============================')
# below is adecrement example that prints the multiples of 3 starting from 201 to 150
number = 201
while number >= 150:
    print(number)
    number = number - 3