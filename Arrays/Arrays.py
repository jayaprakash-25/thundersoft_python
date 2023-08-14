#Arrays
''' Array is a user defined collection of similar data type elements.
 Array index always starts with zero and ends with size – 1'''

'Single array'

# Creating an array
my_array = [1, 2, 3, 4, 5]
print(my_array)


my_array = [10, 20, 30, 40, 50]

# Accessing elements
print(my_array[0])  
print(my_array[3])  


my_array = [10, 20, 30, 40, 50]

# Modifying elements
my_array[2] = 35
print(my_array)  



my_array = [10, 20, 30, 40, 50]

# Finding the length of the array
length = len(my_array)
print(length)  


my_array = [10, 20, 30, 40, 50]

# Adding elements to the end
my_array.append(60)
print(my_array)

# Adding elements at a specific index
my_array.insert(2, 25)
print(my_array)  


my_array = [10, 20, 30, 40, 50]

# Removing an element by value
my_array.remove(30)
print(my_array)  

# Removing an element by index
del my_array[2]
print(my_array)


my_array = [10, 20, 30, 40, 50]

# Iterating through the array
for num in my_array:
    print(num)




























