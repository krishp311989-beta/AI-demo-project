"""
Simple Calculator Program
Performs basic arithmetic operations: Addition, Subtraction, and Division
"""

def addition(num1, num2):
    """
    Adds two numbers together and returns the result.
    
    Args:
        num1 (float): The first number to be added.
        num2 (float): The second number to be added.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2


def subtraction(num1, num2):
    """
    Subtracts the second number from the first and returns the result.
    
    Args:
        num1 (float): The first number (minuend).
        num2 (float): The second number (subtrahend).

    Returns:
        float: The difference between num1 and num2.

    Raises:
        TypeError: If inputs are not numbers.
    """
    return num1 - num2


def division(num1, num2):
    """
    Divides the first number by the second and returns the result.
    Includes a check to prevent division by zero.

    Args:
        num1 (float): The dividend (the number to be divided).
        num2 (float): The divisor (the number to divide by).

    Returns:
        float: The result of num1 divided by num2.

    Raises:
        ValueError: If num2 is zero, as division by zero is undefined.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2


def main():
    """
    The main function that runs the calculator program.
    It provides a menu interface for the user to select operations
    and enter numbers.

    Features:
    - Displays a menu of operations.
    - Takes user input for numbers and operation selection.
    - Validates input and handles errors gracefully.
    - Loops until the user chooses to exit.
    """
    print("=" * 50)
    print("        SIMPLE CALCULATOR PROGRAM")
    print("=" * 50)
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Division (/)")
        print("4. Exit")
        
        # Get user choice and ensure it's a string
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        
        if choice == '4':
            # User chose to exit
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        elif choice in ['1', '2', '3']:
            try:
                # Get input from user for two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform the selected calculation
                if choice == '1':
                    result = addition(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = subtraction(num1, num2)
                    operation = "-"
                else:  # choice == '3'
                    result = division(num1, num2)
                    operation = "/"
                
                # Display the result to the user
                print(f"\n{num1} {operation} {num2} = {result}")
                
            except ValueError as e:
                # Catch cases where user enters non-numeric input
                print(f"\nError: {str(e)}")
        
        else:
            # Handle invalid menu selection
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")


# This block ensures main() runs only if this file is executed directly
if __name__ == "__main__":
    main()#This is sample commit to f2 branch 

#this is just to commit to f4 branch changes 