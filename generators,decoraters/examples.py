#generator
def f1():
    yield "Sai"
    yield 123
    yield "SaiRam"
    yield 123.45

print(type(f1))
for i in f1():
    print(i)


def countdown(n):
    while n > 0:
        yield n
        n -= 1
print(type(countdown))
for num in countdown(5):
    print(num)


even_numbers = (x for x in range(10) if x % 2 == 0)
print(type(even_numbers))
for i in even_numbers:
    print( i)


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

counter = count_up_to(5)
for num in counter:
    print(num)  




#decorator
def mydiv(div):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return div (x,y)
    return inner
@mydiv
def div(a,b):
    return (a/b)

print(div(2,4))


def decor(greet):
    def inner(name):
        if name=="raj":
            print("hello",name,"Good Night")
        else:
            greet(name)
    return inner

@decor
def greet(name):
    print("hello",name,"Good Morning")

greet("balaji")
greet("raj")




































