class Student:
    def __init__(self,x,y,z):
        self.sid=x
        self.sname=y
        self.saddress=z
    def display(self):
        print("Student id is:",self.sid)
        print("Student name is:",self.sname)
        print("Student address is:",self.saddress)
s1=Student(101,"sai","hyd")
s1.display()



#without constructor
class Student:
    def getdata(self):
        self.sid=int(input("enter sid:"))
        self.sname=(input("enter sname:"))
        self.saddress=(input("enter saddress:"))
    def display(self):
        print("Student id is:",self.sid)
        print("Student name is:",self.sname)
        print("Student address is:",self.saddress)
s1=Student()
s1.getdata()
s1.display()

#without method
class Student:
 def __init__(self,x,y,z):
     self.sid=x
     self.sname=y
     self.saddress=z
s1=Student(101,"sai","hyderabad")
print(s1.sid,s1.sname,s1.saddress)

