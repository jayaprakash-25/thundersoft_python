s=lambda n:n*n
print(s(4))

s=lambda a,b:a+b
print(s(10,20))

s=lambda a,b:a+b
print(s(10,20))


s=lambda a,b,c:a if a>b and a>c else b if b>c else c
print(s(2,3,4))



s=lambda n:"is even" if n%2==0 else "is odd"
print(s(5))
print(s(8))


# A lambda function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print(result) 


# Using lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  

# Using lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  

# Lambda function for calculating the area of a rectangle
area_rectangle = lambda length, width: length * width
print(area_rectangle(5, 3))



values = [1, None, 3, None, 5, None, 7]
filtered_values = filter(lambda x: x is not None, values)
print(list(filtered_values))  
