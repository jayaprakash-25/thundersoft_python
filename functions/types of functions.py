'types of functions'
'1.built functions'
'2.user defined functions'
def biggest(a,b):
 if a>b:
     print(a,"is big")
 else:
     print(b,"is big")
biggest(23,45)



def biggest(a,b,c):
 if a>b and a>c:
     print(a,"is big")
 elif b>c:
     print(b,"is big")
 else:
     print(c,"is big")
biggest(2,3,4)
biggest(4,3,2)
biggest(3,4,2)
biggest(4,2,3)


def sum(a,b):
 print("sum is:",a+b)
sum(10,20)
sum(23.4,56.7)
sum(a=int(input("Enter Num1:")),b=int(input("Enter Num2:")))

 
def sum_sub(a,b):
 sum=a+b
 sub=a-b
 return sum,sub
x,y=sum_sub(20,10)
print("sum is:",x)
print("sub is:",y)

 
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x * y
def divide(x, y):
 return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
 print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
 print(num1,"-",num2,"=", 
subtract(num1,num2))
elif choice == '3':
 print(num1,"*",num2,"=", 
multiply(num1,num2))
elif choice == '4':
 print(num1,"/",num2,"=", divide(num1,num2))
else:
 print("Invalid input")
