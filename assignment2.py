# research on if ... else statements in python


# Create a tuple of 8 planets
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

# Print all planets
print("All planets:")
print(planets)

# Print planets from index 2 to 6
print("\nPlanets from index 2 to 6:")
print(planets[2:7])


#else statements in python

#1. Basic if ... else
age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

#if ... elif ... else (multiple conditions)
marks = 65

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")