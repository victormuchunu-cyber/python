# FUNCTIONS WITH PARAMETER.
# Parameters- They are values that get passed as arguments given to a function iside of the parenthesis.


def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("Victor")
greeting("Mary")

print("======================")
def message(names):
    print(f"Hello {names}  We shall be have a general meeing on date.... Please avail Yourself.")

message("Joy")
message("Maleka")


print("======================")
# Create a funcion that accepts parameter to add two numbers.

def addition(a, b):
    sum = a + b
    print("The sum of the numbers is: ", sum)

addition(5, 5)