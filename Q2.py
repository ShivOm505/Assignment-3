'''
Task 2: Using the Math Module for Calculations
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

'''

import math


def sQrt(n):
    return math.isqrt(n)


def loG(n):
    return math.log(n)


def sinE(n):
    return math.sin(n)


n = int(input("Please Enter a number: "))

square_root = sQrt(n)
print("The Square root of the given number is : ", square_root)

loGe = loG(n)
print("The log base e of the given number is : ", loGe)

sine = sinE(n)
print("The sine of the given number is : ", sine)
