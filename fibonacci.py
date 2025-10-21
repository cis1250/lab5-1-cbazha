#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
x = 0
y = 1
def get_user_input():
  inp = int(input("How many terms of the fibonacci sequence do you want?"))
  if (inp <= 0):
    print("Enter a positive integer.")


          
def fibonacci_generator():
  for num in range(inp):  
    x, y = y, x + y



def print_sequence():
  print("Fibonacci sequence: ")
  print(x, y)


get_user_input()
fibonacci_generator()
print_sequence()
