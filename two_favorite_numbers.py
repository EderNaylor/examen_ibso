"""
A program that prompts for two numbers. Add them together and print the result.
Catch the TypeError if either input value is not a number,
and print a friendly error message.
"""


def add_two_numbers():
    try:
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        
        # Convert inputs to integers
        number1 = int(number1)
        number2 = int(number2)
        
        # Add the numbers and print the result
        result = number1 + number2
        print(f"The sum of the numbers is: {result}")
    except ValueError:
        # Handle the case where input is not a number
        print("Error: Please enter numbers only.")


add_two_numbers()
