# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def clean_result(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

while True:
    print("\n=== Simple Calculator ===")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    numb1 = clean_result(num1)
    numb2 = clean_result(num2)

    if choice == '1':
        result = add(num1, num2)
        result = clean_result(result)
        print(f"The sum of {numb1} and {numb2} is {result}.")
    elif choice == '2':
        result = subtract(num1, num2)
        result = clean_result(result)
        print(f"The difference of {numb1} and {numb2} is {result}.")
    elif choice == '3':
        result = multiply(num1, num2)
        result = clean_result(result)
        print(f"The product of {numb1} and {numb2} is {result}.")
    elif choice == '4':
        result = divide(num1, num2)
        result = clean_result(result)
        print(f"The quotient of {numb1} and {numb2} is {result}.")
    else:
        result = "Invalid input"
    
    num1 = None
    num2 = None