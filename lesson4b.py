#  LOOPS => Sometiomes we may need to do a piece of work a number of repeated times in such cases we may use loops.
# A loop is a controlled structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There two types of loops in python i.e., The for loop and the while loop.

# Below is the syntax of a for loop in pyhton.
"""
for variable in range(n):
    # block of code to be executed
"""

# print("Hellow Moses")
# print("Hellow Moses")
# print("Hellow Moses")
# print("Hellow Moses")
# print("Hellow Moses")

for greeting in range(5):
    print("Hello Moses", greeting)


print('================')

for number in range(10, 20):
    print(number)


print('================')
#  find the even numbers in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)


print('================')
# Create a pyton program that prints the odd number from 100 to 150
for number in range(101, 150, 2):
    print(number)


print('================')
#  Create a program that prints the multiples of 3 starting from 201 to 150.
for num in range(201, 149, -1):
    if num % 3 == 0:
        print(num)


print('================')
# Create a python program that prints the leap year in between 2000 and 2024
for number in range(2000, 2025, 4):
    if number % 4 ==0:
        print(number)