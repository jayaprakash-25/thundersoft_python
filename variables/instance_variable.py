class Test:
    def __init__(self):
        self.a=20
        self.b=10
    def m1(self):
        print(self.a)
        print(self.b)
t=Test()
t.m1()
print(t.a)
print(t.b)


#del or changing instance variable
class Test:
 def __init__(self):
     self.a=10
     self.b=20
     self.c=30
 def m1(self):
     del self.a
t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
t1.m1()
del t2.b
t1.c=44
print(t1.__dict__)
print(t2.__dict__)
