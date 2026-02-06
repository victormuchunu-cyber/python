# Create a python program that is able to determine whether a number entered is an odd number or an even number.

number = int(input("Enter Number."))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is Odd")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is greater than 50kgs an dage is above 18 can be able to donate blood else not possible.
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age > 18 and weight > 50:
    print("You are eligible to donate blood")
else:
    print("You are NOT eligible to donate blood")
