'''
 Calculate Factorial Using a Function
 1.   Defines a function named factorial that takes a number as an argument
and calculates its factorial using a loop or recursion.

2.   Returns the calculated factorial.

3.   Calls the function with a sample number and prints the output.

'''


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print("The factorial of the Given number is: ", result)

'''
# Using While Loop for factorial
fact = 1
n = 5
while n > 0:
    fact *= n
    n -= 1

print("The Factorial of the given number is : ", fact)


# Using For loop for factorial
fact1 = 1
n = 5
if n<2:
  print(1)
else:
      for i in range(n):
        fact1*=n
        n-=1
print("The Factorial of the given number is : ", fact1)
'''
