#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_user_input():
    while True:
        try:
            n = int(input("Enter how many terms of the Fibonacci sequence you want: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_sequence(sequence):
    print("Fibonacci sequence:")
    print(", ".join(map(str, sequence)))


# --- Main program ---
def main():
    n = get_user_input()
    sequence = generate_fibonacci(n)
    print_sequence(sequence)


# Run the program
if __name__ == "__main__":
    main()
