def get_number(prompt):
    while True:
        num_input = input(prompt)
        if num_input.replace(".","",1).isdigit():
            return float(num_input)
        print("Only valid numbers are allowed. Try again.")

def get_operator():
    valid_operators = ['+','-','*','/','%','**']
    while True:
        op = input("Enter operation (+, -, *, /, %, **): ")
        if op in valid_operators:
            return op
        print("Invalid operator.Choose one of +, -, *, /, %, **.")

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Note: Cannot divide by 0.")
            return 0
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            print("Note: Cannot use Modulus with 0.")
            return 0
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    

def calculator():
    print("Welcome to the Enhanced CLI Calculator with History & Zero Handling!")

    history = []

    while True:
        num1 = get_number("Enter first number: ")
        operator = get_operator()
        num2 = get_number("Enter second number: ")

        result = calculate(num1, operator, num2)

        print(f"Result: {num1} {operator} {num2} = {result}")

        history.append(f"{num1} {operator} {num2} = {result}")

        show_history = input(" See calculation history? (y/n): ").lower()
        if show_history == 'y':
            print("\nCalculation History:\n")
            for idx, record in enumerate(history,1):
                print(f"{idx}. {record}")
            print()


        again = input(" Do you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye! Thanks for using the CLI calculator.")
            break

calculator()
