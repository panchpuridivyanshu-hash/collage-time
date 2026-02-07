#2.Calculator – A simple calculator that can perform basic arithmetic operations
print("======CALCULATOR======")

# Taking user input
a = int(input("ENTER THE FIRST NUMBER: "))
b = int(input("ENTER THE SECOND NUMBER: "))

# Function Definitions
def sum(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Operation cannot be performed (Division by Zero)"
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

# Calculator Menu
while True:
    print("\n1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. MODULO")
    print("6. EXIT")

    
    Choice = int(input("Choose an option: "))  # Convert input to integer

    if Choice == 1:
        print("RESULT:", sum(a, b))
    elif Choice == 2:
        print("RESULT:", subtraction(a, b))
    elif Choice == 3:
        print("RESULT:", multi(a, b))
    elif Choice == 4:
        print("RESULT:", division(a, b))
    elif Choice == 5:
        print("RESULT:", modulo(a, b))
    elif Choice == 6:
        print("Exiting Calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-6.")
