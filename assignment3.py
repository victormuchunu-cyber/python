# Monthly contribution calculator

gross_salary = float(input("Enter your gross salary: "))

if gross_salary <= 5999:
    contribution = 150
elif gross_salary <= 7999:
    contribution = 300
elif gross_salary <= 11999:
    contribution = 400
elif gross_salary <= 14999:
    contribution = 500
elif gross_salary <= 19999:
    contribution = 600
else:
    contribution = 750

print("Your monthly contribution is:", contribution)