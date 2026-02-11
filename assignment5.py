# Q1 — Function without parameters (Area of rectangle)


def rectangle_area():
    length = 12
    width = 5
    area = length * width
    print("Area of rectangle:", area)

rectangle_area()


# Q2 — Function with parameters (sum, difference, product, division)
def operations(a, b):
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Division:", a / b)

operations(20, 4)
     


# Q3 — If…elif…else (positive, negative, zero)
def check_number():
    num = float(input("Enter a number: "))

    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

check_number()


# Q4 — For loop (sum from 1 to n)
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum from 1 to", n, "is:", total)

sum_to_n(10)


# Q5 — While loop (square from 1 to number)
def square_numbers():
    n = int(input("Enter a number: "))
    i = 1

    while i <= n:
        print("Square of", i, "=", i * i)
        i += 1

square_numbers()
