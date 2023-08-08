"types of arguments"
'''1.positional
   2.keyword
   3.default
   4.variable length'''

#positional arguments
'''The arguments which are passed to a function in correct positional order is 
called positional arguments.'''

def sub(a,b):
 print("sub is:",a-b)
sub(20,10)
sub(10,20)

#keyword arguments
'''The arguments which are passed to a function by using a keyword or 
parameter name are called keyword arguments. '''


def f1(name,msg):
 print("Hello:",name,msg)
#keyword arguments
f1(name="mohan",msg="Good morning")
f1(msg="Good morning",name="mohan")
#positional arguments
f1("mohan","Good morning")
f1("Good morning","mohan")


#default arguments
def f1(name,cource="python"):
 print(name,"course is:",cource)
f1("sai","c")
f1("mohan")
f1("ram")


def f1(cource="python"):
 print("course is:",cource)
f1("c")
f1()

#variable length arguments

def f1(*a):
 print(a)
f1()
f1(10)
f1(10,20)
f1(10,20,30)


def add(*n):
 s = 0
 for i in n:
     s=s+i
 print("sum is:",s)
add(10,20)
add(2,3,4)
add(2,3,4,5,6,7)
add(10,20,30,40,50,60,70)


'we can use *args'
def add(*args):
 s = 0
 for i in args:
     s=s+i
 print("sum is:",s)
add(10,20)
add(2,3,4)
add(2,3,4,5,6,7)
add(10,20,30,40,50,60,70)

'we can use **kwargs'


def f1(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,"=",v)
f1(a=10,b=20,c=30)
f1(eid=1234,ename="sai",eaddress="hyd",esal=45000)





























































































