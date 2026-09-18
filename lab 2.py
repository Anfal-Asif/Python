# # Task 1(While loop)
# count = 0
# while(count<3):
#     count = count + 1
#     print("Hello world")

# # task 2
# count = 0
# while(count == 0):print("hello World")

# # Task 3(list iteration)
# list1 = ["Geeks","for","Geeks"]
# for i in list1:
#     print(i)

# # task4(Tuple iteration)
# print("\n tuple iteration")
# t = ("geeks","for","geeks")
# for i in t:
#     print(i)

# # Task 4(String iteration)  
# print("\nString Iteration")  
# s = "Geeks"
# for i in s:
#     print(i)

# # Task 5(iterating by index of sequence)    
# list = ["Geeks" , "for" ,"geeks"]
# for index in range(len(list)):
#     print( list[index])

# #Task 6(continue Statement)
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#              continue
#     print('Current letter:',letter)

# Task 7(Break)

# for letter in 'geeksforgeeks':
#       if letter == 'e' or letter =='s':
#             break
#       print("Current letter",letter)
      

# TAsk 8(Functions)

# def my_fun():
#     print("Hello world")

# my_fun()    

# # task 9(function with parameters)
# def info(fname):
#     print(fname + "Refsnes")

# info("Anfal")    

# #Task 10(Default parameters)
# def my_fun(country = "Norway"):
#     print("I am from ",country)

# my_fun("Sweden")
# my_fun()   

# # task 11 (passing list as a parameter)
# def my_fun(food):
#     for x in food:
#         print(x)

# fruits = ["Apple ", "Mango" , "Cherry"]
# my_fun(fruits)

# Task12(Return values)
# def my_fun(x):
#     return 5*x

# print(my_fun(3))

# # Task13(keyword arguments)
# def my_fun(child3,child2,child1):
#     print("The youngest child is ",child3)

# my_fun(child1 = "emil", child2 = "Tobis" ,child3 = "linus")

# # Task 14(Creating class)
# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)    

# # Task 15(init_function)
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

# Task 16(object methods)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello my name is ",self.name)

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.greeting()
