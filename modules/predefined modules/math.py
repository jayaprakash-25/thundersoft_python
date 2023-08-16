#predefined modules

'''import math
factorial=math.factorial(5)
print(factorial)

from math import *
print(factorial(5))
print(sqrt(2))
print(pow(3,2))
print(ceil(34.2))
print(floor(34.9))'''

from random import *
for i in range(10):
 print(randrange(2,21,2))

from random import *
l=['sai','hi']
x=choice(l)
print(x)


import datetime
x=datetime.datetime.now()
print(x)


from datetime import *
x=datetime.now()
print(x)
print(x.strftime('%A')) 
print(x.strftime('%a')) 
print(x.strftime('%Y')) 
print(x.strftime('%y')) 


from calendar import *
y=1947
m=8
print(month(y,m))
print(month(2021,11))

from calendar import *
print(calendar(2021))
print(month(1947,8))





























