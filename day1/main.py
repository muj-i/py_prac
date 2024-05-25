number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
operation = input("Enter the operation: ")

def add_numbers():
    if number_1.isnumeric() == False or number_2.isnumeric() == False:
        return "Invalid input. Please enter a number."
    addition = int(number_1) + int(number_2)
    return addition
     

def subtract_numbers():
    if number_1.isnumeric() == False or number_2.isnumeric() == False:
        return "Invalid input. Please enter a number."
    subtraction = int(number_1) - int(number_2)
    return subtraction

def multiply_numbers():
    if number_1.isnumeric() == False or number_2.isnumeric() == False:
        return "Invalid input. Please enter a number."
    multiplication = int(number_1) * int(number_2)
    return multiplication

def divide_numbers():
    if number_1.isnumeric() == False or number_2.isnumeric() == False:
        return "Invalid input. Please enter a number."
    division = int(number_1) / int(number_2)
    return division

if operation == "+":
    addition = add_numbers()
    print("Addition: " + str(addition))
elif operation == "-":
    subtraction = subtract_numbers()
    print("Subtraction: " + str(subtraction))
elif operation == "*":
    multiplication = multiply_numbers()
    print("Multiplication: " + str(multiplication))
elif operation == "/":
    division = divide_numbers()
    print("Division: " + str(division))
else:
    print("Invalid operation. Please enter a valid operation.")