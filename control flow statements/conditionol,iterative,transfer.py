#conditional statements
#if

#program to check the given number is even or odd
i=int(input("Enter a number:"))
if i%2==0:
    print(i,"is even")
else:
    print(i,"is odd")


#program to find biggest of two numbers

i=int(input("Enter num1:"))
j=int(input("Enter num2:"))
if i>j:
 print(i,"is big")
else:
 print(j,"is big")


#program to check the given number is in between 1 and 100
n=int(input("Enter number:"))
if n>=1 and n<=100:
 print("The number",n,"is in between 1 to 100")
else:
 print("The number", n, "is not in between 1 to 100")

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
 # program to find biggest of three numbers
i=int(input("Enter num1:"))
j=int(input("Enter num2:"))
k=int(input("Enter num3:"))
if i>j and i>k:
 print("Biggest number is:",i)
elif j>k:
 print("Biggest number is:",j)
else:
 print("Biggest number is:",k)

#Iterative statements
#for
 'program to display even numbers from 0 to 20'

 for i in range(21):
     if i%2==0:
         print(i)


'program to display sum of first n numbers'
n=int(input("Enter number:"))
sum=0
for i in range(n+1):
 sum=sum+i
print("sum of first",n,"numbers:",sum)

#while
'program to display sum of first n numbers'
n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
 sum=sum+i
 i+=1
print("Sum of first",n,"numbers is:",sum)


#Transfer Statements
#break
for i in range(10):
 if i==5:
     break
 print(i)

#continue
 for i in range(10):
     if i==5:
         continue
     print(i)

 #pass
 i=10
if i==10:
 pass
else:
 pass

 



