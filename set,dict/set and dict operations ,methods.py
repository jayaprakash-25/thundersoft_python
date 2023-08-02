#Working with set()
'creating a set'
s=set()
print(s)
print((type(s)))

#add and update
s={1,2,3,"hi",3}
s.add(9)
print(s)
s.update([99,00,77])
print(s)

#discrd,remove,clear
s={1,2,3,4,5}
s.discard(2)
print(s)
s.remove(1)



#set operators:union,intersection,difference,symmetric diff
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A&B)
print(A-B)
print(B-A)
print(A^B)

'set len,max,min,sum'
s={10,34.5,-45,89,99}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sum(s,9))

'Set membership test'
s={10,34.5,-45,89,99}
print(10 in s)
print(9 in s)
print(99 not in s)

#Working with dict functions
'creating a dict'

d={}
print(d)
print(type(d))

'access value from dict'

d={"hi":1,"hello":2}
print(d.get("hello"))
print(d["hello"])

d={"hi":1,"hello":2}
d["hello"]="3"
print(d)

'deleting'

d={"hi":1,"hello":2}
del d["hello"]
print(d)

'dict copy'
d={1:"jp",2:"sai"}
d1=d.copy
print(d1)
d[1]="kav"
print(d1)
print(id(d1))

'dict items,keys,values'
d={1:"sai",2:"mohan",3:"raja"}
print(d.items())
print(d.keys())
print(d.values())


#dict len and membership test
d={1:"hi",2:"jio"}
print(len(d))
print(1 in d)

'dict popitem and popmethods'
d={1:"sai",2:"mohan",3:"durga"}
print(d.pop(1))
print(d)
print(d.popitem())
print(d)


#byte and byte array
x=[10,20,30,40]
b=bytearray(x)
print(b)
print(type(b))



'''frozen set is similar to set but only difference is set is
mutable where as frozen set is immutable'''


#FUNCTIONS#
'''TWO TYPES OF FUNCTIONS 
      .built in functions
      .user defined functions'''



def f1():
    for i in range(10):
        print("Hello")
f1()

def iseven(n):
    if(n%2==0):
        print(n,"is even")
    else:
        print(n,"is odd")
iseven(5)


def biggest(a,b):
    if a>b:
        print(a,"is big")
    else:
        print(b,"is big")
biggest(12,10)




def add(a,b):
    print(a+b,"sum is:")
add(1,2)










































