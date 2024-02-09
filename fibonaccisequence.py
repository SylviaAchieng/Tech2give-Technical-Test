"""
Write a program to generate the Fibonacci sequence up to 100.
"""


def gen_fibonacci(limit):
    fib_sequence = [0, 1] 
    
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

limit = 100


fibonacci_sequence = gen_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)
