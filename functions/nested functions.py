def outer_function():
    print("This is outer function")

    def inner_function():
        print("This is inner function")
    inner_function()
outer_function()



def outer_function(x):
    print("Outer function received:", x)

    def inner_function(y):
        print("Inner function received:", y)

    inner_function(x + 5)

outer_function(10)

def outer_function(x):
    print("Outer function received:", x)

    def inner_function(y):
        return y * 2

    result = inner_function(x + 5)
    print("Inner function returned:", result)

outer_function(10)


def outer_function(x):
    print("Outer function received:", x)

    def inner_function(y):
        return x + y

    result = inner_function(5)
    print("Inner function result:", result)

outer_function(10)


def outer_generator(limit):
    def inner_generator():
        for i in range(limit):
            yield i * 2
    return inner_generator()

gen = outer_generator(5)
for value in gen:
    print(value)













































