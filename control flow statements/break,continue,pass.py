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
    print(i)


i=1
while i<=10:
    print(i)
    i+=1
    if i==5:
        i+=1
        continue


num=1
while i<=5:
    print(num)
    i+=1
