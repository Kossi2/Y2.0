# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 // 9

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 // 5) + 32

# Welcome and greet user
print("Welcome to the Temperature Converter!")
guest_name = input("Please enter your name: ")
print(f"Hello, {guest_name}! Let's start converting temperatures.")

while True:
    # Ask if the user wants to convert to Fahrenheit or to Celsius
    conversion_type = input("Do you want to convert temperature to Fahrenheit or to Celsius? (F/C): ").lower()
    
    if conversion_type == 'f':
        # Get user input
        celsius = int(input("Enter temperature in Celsius: "))

        # Convert to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)

        # Display the result
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
    elif conversion_type == 'c':
        # Get user input
        fahrenheit = int(input("Enter temperature in Fahrenheit: "))

        # Convert to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)

        # Display the result
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
    else:
        print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

    # Ask if the user wants to do another conversion
    another_conversion = input("Do you want to do another conversion? (yes/no): ").lower()
    if another_conversion != 'yes':
        print(f"Goodbye, {guest_name}!")
        break