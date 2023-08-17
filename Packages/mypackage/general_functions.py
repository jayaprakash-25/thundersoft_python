def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def iseven(n):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")


def biggest(a,b,c):
    if a>b and a>c:
        print(a,"is big")
    elif b>c:
        print(b,"is big")
    else:
        print(c,"is big")


def sqrt(n):
    print("square is:",n*n)
