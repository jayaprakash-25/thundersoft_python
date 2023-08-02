name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.", end=" ")
print("Nice to meet you!")

'office day 3'
a="jp"
b="gasarlu"
c="vihari homes"
print("my name is",a,"s/o",b,"address",c,)

'eval function'
'it directly take int,float with out entering'

a=eval(input("enter a value: "))
print(a)
b=(input("enter b value: "))
print(b)


'operaters'
'arithematic'
print(2+3)
print(4-1)
print(5*2)
print(5**2)
print(5/2)
print(5//2)
print(5%2)

'relation'
print(3<4)
print(4>5)
print(4<=4)
print(5>=5)
print(3==3)
print(3!=3)

'assignment'
a=5
print(a)
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)
a**=2
print(a)
a%=2
print(a)

'logical'
print(2<3 and 4<5)
print(2<3 and 4>5)
print(2<3 or 4>5)
print(2<3 or 1<2)
print(1>2 or 2>3)
print(not(2<3))
print(not(1>2))

'membership in,not in'
lst=[2,3,4,5]
print(2 in lst)
print(100 in lst)
print(100 not in lst)
print(2 not in lst)

'identity is, is not'
a=2
b=2
print(a is b)

'id()'
a=2
b=2
print(id(a))
print(id(b))

'bitwise'
a=9
b=5
print(bin(a))
print(bin(b))
print(bin(a&b))
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)

#control flow statements
'''conditional statements(if,else,elif,nested if)
 iterative statements(for loop,while loop)
 transfer statements(break,continue,pass)'''

#conditional statements
#if
i=100
if i==100:
    print(True)

#if else
i=100
if i==100:
    print(True)
else:
    print('false')
#program for even number
n=int(input("enter the number: "))
if n%2==0:
    print("the given number",n, "is even")
else:
    print("the given number",n,"is not even")


#program for finding biggest number
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
    print(a,"is bigger")
else:
    print(b,"is bigger")

#nested if
i=int(input("Enter num1:"))
j=int(input("Enter num2:"))
if i>j:
 print(i,"is greater than",j)
else:
 if i<j:
     print(i,"is less than ",j)
 else:
     print(i,"is equal to",j)
 
 #elif
 #program to find biggest of three numbers

i=int(input("Enter num1:"))
j=int(input("Enter num2:"))
k=int(input("Enter num3:"))
if i>j and i>k:
    print("Biggest number is:",i)
elif j>k:
    print("Biggest number is:",j)
else:
    print("Biggest number is:",k)

#iterative statements
    #for loop


l=[10,20,30,40,50,60]
for i in l:
    print(i,end=' ')









 
