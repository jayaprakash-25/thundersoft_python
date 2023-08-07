def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")


def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)


def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def hello_world():
    print("Hello, World!")

hello_world()


def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar"))


def reverse_string(s):
    return s[::-1]

print(reverse_string("Python is fun"))

def list_sum(nums):
    return sum(nums)

numbers = [10, 20, 30, 40, 50]
print(list_sum(numbers))
