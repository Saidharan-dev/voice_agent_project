# simple_addition.py

def add_numbers(num1, num2):
    """
    Adds two numbers together.

    Args:
        num1 (float): The first number to add.
        num2 (float): The second number to add.

    Returns:
        float: The sum of the two input numbers.
    """
    return num1 + num2

# Example usage
if __name__ == "__main__":
    num1 = 5.0
    num2 = 7.0
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")