#Function variables

'local variables'


def f1():
    a=10
    print(a)

f1()

def add_numbers(a,b):
    result=a+b
    return result
print(add_numbers(5,7))


def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print(celsius_to_fahrenheit(25))


def max_of_three(a,b,c):
    max_value=max(a,b,c)
    return max_value
print(max_of_three(4,5,6))


def string_length(s):
    length = len(s)
    return length

print(string_length("Hello, world!"))


def area_of_circle(r):
    pi=3.14
    area=pi*r**2
    return area
print(area_of_circle(4))


def reverse_list(list):
    reversed_list=list[::-1]
    return reversed_list
print(reverse_list([1,2,34,4,5]))




def is_palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]

print(is_palindrome("a man a plan a canal panama"))


def triangle_area(b,h):
    area=0.5*b*h
    return area
print(triangle_area(2,6))

def min_of_three(a,b,c):
    min_value=min(a,b,c)
    return min_value
print(min_of_three(1,2,3))


'global variables'

a=10
def f1():
    print(a)
def f2():
    print(a)

f1()
f2()


def f1():
 global a
 a=99
 print(a)
def f2():
 print(a)
f1()
f2()

a=10
def f1():
 a=20
 print(a)
 print(globals()['a'])
def f2():
 print(a)
f1()
f2()



class MyClass:
    global_var = 10

    def print_global(self):
        print(self.global_var)

obj = MyClass()
obj.print_global()



global_var = 10

def print_global():
    print(global_var)

print_global()



global_var = 10

def check_global():
    global global_var
    if global_var > 5:
        print("Global variable is greater than 5")

check_global()




global_var = 110

def scope_example():
    global_var = 120  # This is a local variable
    print(global_var)

scope_example()  # Output: 120
print(global_var)  # Output: 110




global_var = 30

def print_global():
    print(global_var)




global_var = 10

def increment_global():
    global global_var
    global_var += 1

increment_global()
print(global_var)  # Output: 11












































