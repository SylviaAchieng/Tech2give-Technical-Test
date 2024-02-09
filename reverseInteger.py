"""Write a program that takes an integer as input and returns an integer with reversed digit
ordering"""

def reverse_integer_hard_way(num):
    reversed_num = 0
    is_negative = False

    if num < 0:
        is_negative = True
        num = abs(num)

    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10

    return -reversed_num if is_negative else reversed_num

# Example usage
print(reverse_integer_hard_way(500))  
print(reverse_integer_hard_way(-56))  
print(reverse_integer_hard_way(-90))  
print(reverse_integer_hard_way(91))   
