run = True # this variable controls if the program repeats
while run:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: ")) # prompts the user to input two numbers, also makes them integers
    print(" [+] [-] [/] [*]")
    operator = input("What would you like to do to these numbers:") # prompts the user to input a mathematical operator
    if operator == "+": # checks the user input
        result = num1 + num2 # adds the value of num1 and num2 together to store in result
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    else:
        print("Invalid operator") # checks if the user enters an invalid input when asked to provide a mathematical operator
    print(result) # prints the value stored in the variable result
    finish = input("Do you want to continue? (y/n): ")
    if finish == "n":
        run = False # asks the user if they want to continue, stops if "n" is entered but keeps running otherwise
    elif finish == "y":
        run = True
    else:
        print("Invalid input")