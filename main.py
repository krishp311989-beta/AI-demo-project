"""
Simple Calculator Program
Performs basic arithmetic operations: Addition, Subtraction, and Division
"""


def addition(num1, num2):
    """
    Adds two numbers and returns the result.
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Sum of num1 and num2
    """
    return num1 + num2


def subtraction(num1, num2):
    """
    Subtracts num2 from num1 and returns the result.
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Difference of num1 and num2
    """
    return num1 - num2


def division(num1, num2):
    """
    Divides num1 by num2 and returns the result.
    
    Args:
        num1: First number (dividend)
        num2: Second number (divisor)
    
    Returns:
        Result of num1 divided by num2
    
    Raises:
        ValueError: If num2 is zero
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2


def main():
    """
    Main method that runs the calculator program.
    Provides a menu for user to select operations.
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
        
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        
        if choice == '4':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        elif choice in ['1', '2', '3']:
            try:
                # Get input from user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform calculation
                if choice == '1':
                    result = addition(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = subtraction(num1, num2)
                    operation = "-"
                else:
                    result = division(num1, num2)
                    operation = "/"
                
                # Display result
                print(f"\n{num1} {operation} {num2} = {result}")
                
            except ValueError as e:
                print(f"\nError: {str(e)}")
        
        else:
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
