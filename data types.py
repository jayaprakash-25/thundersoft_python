a=None
print(a)
print(type(a))


'1.int'
a=10
print(a)
print(type(a))

'2.float'
a=10.9
print(a)
print(type(a))


'convert from int to float'
a=10
print(a)
print(type(a))

b=float(a)
print(b)
print(type(b))

'convert from float to int'
a=10.8
print(a)
print(type(a))

b=int(a)
print(b)
print(type(b))

'3.complex'
a=9
b=8
c=complex(a,b)
print(c)
print(type(c))
print(c.real)
print(c.imag)

'4.bool'
a=5
b=6
c=a<b
print(c)
print(type(c))
print(int(c))
print(int(True))
print(int(False))
print(True+True)
print(4+True)

'5.string'
s="durgasoft"
print(s)
print(type(s))
s='durga\'s'
print(s)
s='''durgasoft
hyderabad
maitrivanam'''
print(s)
s="""durgasoft
hyderabad
maitrivanam"""
print(s)

'6.list'
l= [10,10,"durga",23.4,20,'A']
print(l)
print(type(l))

'7.tuple'
t=(10,10,"durga",23.4,20,'A')
print(t)
print(type(t))

'8.set'
s=set()
print(s)
print(type(s))


s={10,"sai",12.4,'A',10}
print(s)
print(type(s))

'9.dict'
d={}
print(d)
print(type(d))

d={1:"sai",2:"mohan",'a':'apple',3:34.5,1:"mohan"}
print(d)
print(type(d))

'10.range'
a=range(10)
print(a)
print(type(a))
