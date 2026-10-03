# Program 1
# Number divisible by 7 and multiple of 5

# for i in range(1500,2701):
#     if i % 7 == 0 and i %  5 == 0:
#         print(i)

#program 2
# celsius and farenheit conversion 

# c = float(input("Enter celsius: "))
# f = (c * 9/5) + 32 
# print(c, "C is", f, "Fahrenheit")

# f = float(input("Enter Fahrenheit: "))
# c = (f - 32) * 9/5
# print(f,"F is ",c, "Celsius")

# program 3
# Guess a number between 1 and 9

# number = 5

# while True:
#     guess = int(input("Guess a number between 1 and 9: "))

#     if guess == number:
#         print("well guessed!")
#         break
#     else:
#         print("Wrong guess. Try again.")

# program 4
# Star pattern

# for i in range(1,6):
#     for j in range(i):
#         print("*",end = " ")
#     print()

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end = " ")
#     print() 

# program 5
# Reverse a word

# word = input("Enter a word: ")
# reverse = word[::-1]
# print("Reverse :" ,reverse)

# Program 6            
# Count enven and odd numbers
# numbers = (1,2,3,4,5,6,7,8,9)

# even = 0
# odd = 0
# for number in numbers:
#     if number % 2 == 0:
#        even = even + 1
#     else:
#         odd = odd +1 

# print("Even numbers :", even)
# print("Odd numbers: " ,odd)          


# program 7
# print item and its type

# datalist = [123 , 11.22 ,1+2j ,True ,'W3schools' ,(0,-1) ,[1,2],{"Class":"V","section":"A"}]
# for item in datalist:
#     print(item,"->",type(item))

# Program 8
# print 0 to 6 except 3 and 6
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# program 9
# Fibonacci series between 0 And 50

# a = 0
# b = 1
# while a <= 50:
#     print(a, end = " ")
#     c = a+b
#     a = b
#     b = c   

#  For understanding   
# for round 1:
#     a = 0
#     b= 1  print a = 1
#     c = a+b = 1
#     a = 1
#     b = 1  
# For round 2:
#     a = 1
#      b =1
#     print a = 1
#      c = a+b = 2
#     a = 1
#     b = 2
# for round 3:
#     a = 1
#     b = 2
#     print a = 1
#     c = a+b= 3
#     a = 2
#     b = 3
# for round 4:
#     a = 2
#     b = 3
# print a = 2
#     c = a+b = 5
#     a = 3
#     b = 5

# # PRogram 10
# # Fizzbuzz(3f, 5b)
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i%3 == 0:
#         print("fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# program(take input from user and print in lower characters)
# while True:
#     line = input("Enter line: ")

#     if line == "":
#         break

#     print(line.lower())

#program 11(2D array)

# m = 3
# n = 4
# array = []
# for i in range (m):
#      row = []

#      for  j in range (n):
#         row.append(i*j)

#      array.append(row)

# print(array)

# program 12
# numbers = input("Enter  binary numbers separated by comma: ")
# numbers = numbers.split(",")
# result = []

# for number in numbers:
#     decimal = int(number,2)
#     if decimal % 5 == 0:
#          result.append(number)
# print(",".join(result))

# Program 13
# count letters and digits
# text = input("Enter a string: ")
# letters = 0
# digits = 0

# for character in text:
#     if character.isalpha():
#         letters = letters + 1

#     elif character.isdigit():
#         digits = digits + 1

# print("Letters :", letters)
# print("Digits: " ,digits)    
#    

# program 14
# Password validation
password = input("Enter a password : ") 
lower = 0
upper = 0
digit = 0
special = 0

for character in password:
    if character >= 'a' and character <= 'z':
        lower = lower + 1
    elif character >= 'A' and character <= 'Z':  
        upper = upper + 1
    elif character >= '0' and character <= '9':
        digit = digit + 1
    elif character == '@' or character =="$" or character == '#':
        special = special + 1

if  len(password) >= 6 and len(password) <= 16:
    if lower >= 1 and upper >=1 and special >=1 and digit >= 1:
            print("Valid Password")
    else:
            print("Invalid Password")
else:
        print("Invalid password")                



