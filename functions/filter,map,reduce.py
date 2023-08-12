#filter

L=[2,3,4,5,6,7,8,9,10]
L1=list(filter(lambda x:x%2==0,L))
print(L1)

words = ["apple", "banana", "grape", "orange", "kiwi"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words) 


mixed_numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))
print(positive_numbers)  


strings = ["hello", "", "world", "", "python"]
non_empty_strings = list(filter(lambda s: s != "", strings))
print(non_empty_strings)  

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]
young_people = list(filter(lambda person: person["age"] < 30, data))
print(young_people)  

#map


L=[2,3,4,5,6,7,8,9,10]
L1=list(map(lambda x:2*x,L))
print(L1)


l=[1,2,3,4,5]
squared_numbers=list(map(lambda x:x**2,l))
print(squared_numbers)

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)

names = ['alice', 'bob', 'charlie']
capitalized_names = list(map(str.capitalize, names))
print(capitalized_names)

numbers = [1, 2, 3, 4, 5]
even_or_odd = list(map(lambda x: 'Even' if x % 2 == 0 else 'Odd', numbers))
print(even_or_odd)


#reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)


numbers = [2, 3, 4, 5]
product_result = reduce(lambda x, y: x * y, numbers)
print(product_result)


numbers = [10, 5, 20, 15]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(max_result)


words = ["Hello", " ", "world", "!"]
concatenated_result = reduce(lambda x, y: x + y, words)
print(concatenated_result)


n = 5
factorial_result = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial_result)

numbers = [1, 2, 3, 4, 5]
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print(sum_of_squares)


L=[10,20,30,40,50,60,70]
result=reduce(lambda x,y:x+y,L)
print(result)



































