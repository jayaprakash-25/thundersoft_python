def f1():
 print("Hello")
f2=f1 
f2()

def original_function():
    print("this is original")
alias_function=original_function
alias_function()


import math
alias_sqrt=math.sqrt
print(alias_sqrt(25))



def add(a, b):
    return a + b
sum_function = add
result = sum_function(3, 5)  
print(result)


def original_function():
    print("Original function")
def new_function():
    print("New function")
func = original_function
func() 
func = new_function  
func()  
