#Working with List functions:
'List index'
l=[10,20,"sai",30,40,"durga",'A',23.4,50,60]
print(l[1])
print(l[-1])
print(l[-4])
print(l[1:6])


l=[10,20,"sai",[30,40,"durga"],'A',23.4,50,60]
print(l[3])
print(l[3][1])
print(l[-5][-2])

#List slice
l=[10,20,"sai",30,40,"durga",'A',23.4,50,60]
print(l[1:5])
print(l[:4])
print(l[1:])
print(l[:])

#Adding elements to the List : insert, append, extend
l=[2,3,4]
print(l)
l.insert(1,33)
print(l)
l=[2,3,4]
print(l)
l.append(33)
l.extend([45,67,89,"sai"])
print(l)

#delete elemnts from list :remove,pop,del

l=[10,20,30,40,50]
l.remove(20)
print(l)
l.pop(3)
print(l)


l=[10,20,30,40,50]
l.pop(2)
print(l)

#List concatenation and multiplication
l1=["sai","durga","ram"]
l2=[10,20,30]
print(l1+l2)
print(l1*3)

l=[2,6,9,4,3,5,7,1]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)


#Working with tuple functions:
t=(10,100)
print(10 in t)
print(100 in t)
print(100 not in t)


# Tuple Len, max, min, sum
t=(10,20,-34,23.4,50)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t,4))

#Converting a string into tuple
s="durga"
t=tuple(s)
print((type(t)))

#Converting a List into tuple
l=[10,20,30,40]
print(l)
print(type(l))
t=tuple(l)
print(t)
print(type(t))

#Tuple packing and unpacking

#packing
a=10
b=20
c=30
t=a,b,c
print(t)
print(type(t))
#unpacking
t=(100,200,300)
a,b,c=t
print("a=",a)
print("b=",b)
print("c=",c)

























