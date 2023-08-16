x=123
def add(a,b):
    print("sum is:",a+b)
def mul(a,b):
    print("mul is:",a*b)
def sub(a,b):
    print("sub is:",a-b)

def f1():
    if __name__=='__main__':
        print("Executed as an individual program")
    else:
        print("Executed from some other program")
f1()
