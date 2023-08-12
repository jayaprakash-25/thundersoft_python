#recursive function

'a function that calls itself is known recursive function'
def factorial(n):
 if n==0:
     result=1
 else:
     result=n*factorial(n-1)
 return result
print("Factorial of 4 is:",factorial(4))
print("Factorial of 5 is:",factorial(5))


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))


def sum_of_natural_numbers(n):
    if n<=0:
        return 0
    else:
        return n+sum_of_natural_numbers(n-1)
print(sum_of_natural_numbers(5))


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18))


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(4))
