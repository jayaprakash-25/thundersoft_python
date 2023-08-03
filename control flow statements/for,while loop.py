#iterative statements

'''for loop
   while loop'''

'1.for loop examples'

'''for i in range(21):
    if i%2==0:
        print(i)


n=int(input("enter the number"))
sum=0
for i in range (n+1):
    sum=sum+i
print("sum of first",n,"numbers is",sum)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for i in range(2, 21, 2):
    print(i)

    
num=8
for i in range (1,11):
    print(num,"x",i,"=",num*i)


n = 5
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum:", sum)

n=int(input("enter no of rows:"))
for i in range (1,n+1):
    print("+" * i)

n=int(input("enter the number"))
factorial=1
for i in range (1,n+1):
    factorial=factorial*i
print("factorial:",factorial)


n = 10
fibonacci = [0, 1]
for i in range(2, n):
    next_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_num)
print("Fibonacci:", fibonacci)


word = "Python"
for char in word:
    print(char)

num=2
for i in range (2,21):
    print(num)
    num=num+2


#for loop is used when the number of iterations is known, whereas execution
is done in the while loop until the statement in the program is proved wrong

#while loop





n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
 sum=sum+i
 i+=1
print("Sum of first",n,"numbers is:",sum)


#Print even numbers from 2 to 20 using a while loop:
num=2
while num<=20:
    print(num)
    num=num+2


num=8
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1

rows=4
i=1
while i<=rows:
    print("+" *i)
    i=i+1


n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("Factorial:", factorial)




n = 10
fibonacci = [0, 1]
i = 2
while i < n:
    next_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_num)
    i += 1
print("Fibonacci:", fibonacci)


word = "Python"
i = 0
while i < len(word):
    print(word[i])
    i += 1


#transfer statements
'break'

for i in range(10):
 if i==5:
     break
 print(i)


i=0
while i<=10:
    print(i)
    i=i+1
    if i==5:
        break


for i in range(10):
    if i==5:
        continue
    print(i)'''

i=1
while i<=10:
    print(i)
    i+=1
    if i==5:
        i+=1
        continue















































