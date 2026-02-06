# A dictionary is a data type that store data in terms of key - value pair.
# It is introduced by the use of curly braces{}.
# The values stored inside a dictionary can be ofaany type.
# To acess the values in a dictionary we use the keys.



phonebook = {
    "Benson" : "254722961336",
    "Mary" : "254795663485",
    "Victor" : "25426104329"
}

#showing the enitire dictionary
print(phonebook)
print(type(phonebook))

# print out Benson's number
print(phonebook["Benson"])

print('==================')

player = {
    "Name" : "Messi",
    "Age" : 40,
    "Teams" : ["PSG", "Barcelona", "Argetina"],
    "More" : {
        "Children" : 3,
        "Residence" : "USA",
        "Phone" : (254798778566,2546609234,25498232359)
    }
}
# Print Barcelona- the second team he played for
print(player["Teams"][1])

#Print Messi's second number.
print(player["More"]["Phone"][1])