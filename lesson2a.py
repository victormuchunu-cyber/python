#Python Lists
# A list in  python is a collection of items that are ordered in a certain way.
# A list is introduced by the use of the square brackets[].
#The items of a list are stored inside of indexes. Note : in programming we start counting from index zero.
# index ero (0). bmw, benz, hiance...
# A list is mutable i.e, the contents of a list can be changed.

cars = ["BMW", "Benz", "Hiance", "LX600", "Tourbillion", "X8", "Sport SVR" ]

print(cars)
print(type(cars))

#Accessing items of a list
print(cars[2])
print("The cars in index four is: ",cars[4])

# List slicing- This is creating a list from a given figure list.
print(cars[4:])

# Printing form index zero to three
print(cars[:4])

# Printing from hiance to tourbillion
print(cars[2:5])

# List Mutability
# We use the function append to add an itemat the end of a list.
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

#  We use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# We can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

# We can use the sort function to sort out the items in alphabetical order.
cars.sort(reverse=True)
print(cars)


# we can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)
del cars[4]
print(cars)
cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)