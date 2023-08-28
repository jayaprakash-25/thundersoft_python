#class and object creation in python

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class person:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
p1=person("jp","21","4r1")
print(p1.name)
print(p1.age)
print(p1.rollno)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")
print(car1.make,car1.model)
print(car2.make,car2.model)



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 3)
print(rectangle1.width,rectangle1.height)
print(rectangle2.width,rectangle2.height)



class Circle:
    def __init__(self, radius):
        self.radius = radius

circle1 = Circle(5)
print(circle1.radius)


class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

animal1 = Animal("Dog", "Woof")
print(animal1.species,animal1.sound)



class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

account1 = BankAccount("12345", 1000)
print(account1.account_number,account1.balance)



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Harry Potter","J.K. Rowling")
print(book1.title,book1.author)



























