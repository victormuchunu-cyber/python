# On th etry and except block: You can sun some codes/statements and if it is successful the try bock will get executed other the except bock will be executed there is an anticipated error.

try:
    number = 100 
    answer = number / 0
    print("The answer is: ", answer)
except Exception as e:
    print("There is an error: ", e)

  