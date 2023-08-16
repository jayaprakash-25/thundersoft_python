import sample
print (sample.x)
sample.add(10,20)
sample.mul(20,30)

import sample as sm
print(sm.x)
sm.add(1,2)
sm.mul(3,4)

import sample
sample.sub(30,20)

from sample import x,add,mul,sub
print(x)
add(1,2)
mul(3,2)
sub(3,2)


from sample import x as a,add as sum
print(a)
sum(2,3)

import sample
sample.f1()
