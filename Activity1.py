try:
    number=int(input("Enter any number"))
    print("The number is:" , number)
except ValueError as ex:
    print("The exection is :" , ex)