print("Welcome to the Simple Calculator!")
guest_name = input("Please enter your name: ")
print(f"Hello, {guest_name}! You can use operations: +, -, *, /, %")

while True:
    try:
        # Get user inputs
        first_number = int(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        second_number = int(input("Enter the second number: "))

        # Perform the calculation
        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        elif operator == '/':
            if second_number != 0:
                result = first_number / second_number
            else:
                result = "Error: Division by zero is not allowed."
        elif operator == '%':
            if second_number != 0:
                result = first_number % second_number
            else:
                result = "Error: Division by zero is not allowed."
        else:
            result = "Invalid operator. Please use +, -, *, /, or %."

        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

    # Ask if the user wants to calculate again
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print(f"Goodbye, {guest_name}!")
        break