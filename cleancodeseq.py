def fibonacci_list(n):
    """Return a list containing the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    """for _ in range(n):
    In Python, _ is just a normal variable name.
    You're looping n times, but you never actually use the 
    loop variable, so instead of writing:
    
    for i in range(n):
    and ignoring i, you write _ to signal:

“I need to loop n times, but the variable inside 
the loop doesn’t matter.”
"""
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def fibonacci_generator(n):
    """Yield the first n Fibonacci numbers one at a time."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    print("Using list version:")
    for num in fibonacci_list(5):
        print(num)

    print("\nUsing generator version:")
    for num in fibonacci_generator(5):
        print(num)


if __name__ == "__main__":
    main()
