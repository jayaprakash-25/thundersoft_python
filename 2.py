#simple if examples
'eg:1'
number = 10
if number > 0:
    print('Number is positive.')
print('The if statement is easy')

'eg:2'
num = 5
if num > 0:
    print("Number is positive")


num = 6
if num % 2 == 0:
    print("Number is even")

text = ""
if not text:
    print("String is empty")


my_list = [1, 2, 3]
if my_list:
    print("List is not empty")



a = 10
b = 10
if a == b:
    print("Numbers are equal")

num = 25
if 20 <= num <= 30:
    print("Number is between 20 and 30")

char = 'e'
if char in 'aeiouAEIOU':
    print("Character is a vowel")

num = 12
if num % 2 == 0 and num % 3 == 0:
    print("Number is divisible by both 2 and 3")

user_role = "admin"
if user_role == "admin":
    print("User has admin privileges")



#if  else examples
num = 7
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")



a = 10
b = 15
if a > b:
    print("Max is", a)
else:
    print("Max is", b)



age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote yet")


year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


text = "racecar"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


#elif examples

char = '7'
if char.isalpha():
    print("Character is a letter")
elif char.isdigit():
    print("Character is a digit")
else:
    print("Character is neither a letter nor a digit")


x = 15
y = 20
z = 10
if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z
print("Largest number is:", largest)


num = -5
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("Your grade is:", grade)


weight = 70  # in kilograms
height = 1.75  # in meters
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print("Your BMI category is:", category)


side1 = 5
side2 = 5
side3 = 5
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"
print("The triangle is:", triangle_type)


weight = 4.7  # in kilograms
if weight <= 1:
    shipping_method = "Standard"
elif weight <= 5:
    shipping_method = "Express"
else:
    shipping_method = "Priority"
print("Recommended shipping method:", shipping_method)


#nested if examples

num = 7
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
        if num % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")
else:
    print("Number is negative")


score = 85
attendance = 90
if attendance >= 80:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
    print("Your grade is:", grade)
else:
    print("Attendance is low, grade not calculated")



x = 2
y = 3
if x > 0:
    if y > 0:
        print("Point is in Quadrant I")
    else:
        print("Point is in Quadrant IV")
else:
    if y > 0:
        print("Point is in Quadrant II")
    else:
        print("Point is in Quadrant III")



year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        print("Year is divisible by 100")
    else:
        print("Leap year")
else:
    print("Not a leap year")


char = '5'
if char.isalpha():
    if char.isupper():
        print("Character is an uppercase letter")
    else:
        print("Character is a lowercase letter")
elif char.isdigit():
    print("Character is a digit")
else:
    print("Character is neither a letter nor a digit")



import math
num = 9
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
        if math.isqrt(num) ** 2 == num:
            print("Number is a perfect square")
else:
    print("Number is negative")








































