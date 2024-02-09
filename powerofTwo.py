"""
Write a program that takes an integer as input and returns true if the input is a power of two
"""

def is_power_of_two(num):
    
    if num <= 0 or type(num) is not int:
        return False

    
    return bin(num).count('1') == 1


user_input = input("Enter an integer: ")

try:
    
    user_integer = int(user_input)

    
    result = is_power_of_two(user_integer)
    print(f"{user_integer} is a power of two: {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
