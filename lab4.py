# # Task 1(STack implementation)

# # stack = []

# # #push
# # stack.append(10)
# # stack.append(20)
# # stack.append(30)

# # print("Stack:",stack)

# # #pop
# # item = stack.pop()
# # print("Removed:", item)

# # print("Stack after pop:",stack)

# # #peak
# # print("Top element:",stack[-1])

# # if len(stack) == 0:
# #     print("Stack is empty")
# # else:
# #     print("Stack is not empty")    
# class Stack:
#     def __init__(self):
#         self.stack = []

#     # Add an element
#     def push(self, item):
#         self.stack.append(item)
#         print(item, "pushed into stack")

#     # Remove the top element
#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack is empty")
#         else:
#             item = self.stack.pop()
#             print(item, "popped from stack")

#     # Display the top element
#     def peek(self):
#         if len(self.stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Top element:", self.stack[-1])

#     # Display all elements
#     def display(self):
#         if len(self.stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Stack:", self.stack)


# # Main program
# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# s.display()

# s.peek()

# s.pop()
# s.display()

# s.pop()
# s.display()

# #task 2(Queue implementation)

# # queue = []

# # #enqueue
# # queue.append(10)
# # queue.append(20)
# # queue.append(30)

# # print("queue: " ,queue)

# # #Front ..or 1st element
# # print("Front element: ",queue[0])

# # #Dequeue
# # print("Removed: " ,queue.pop(0))
# # print("Queue after dequeue: " ,queue)

# # if len(queue) == 0:
# #     print("Queue is empty")
# # else:    
# #     print("Queue is not empty")

# class Queue:
#     def __init__(self):
#         self.queue = []

#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)
#         print(item, "added to queue")

#     # Remove the first element
#     def dequeue(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             item = self.queue.pop(0)
#             print(item, "removed from queue")

#     # Display the first element
#     def front(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             print("Front element:", self.queue[0])

#     # Display all elements
#     def display(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             print("Queue:", self.queue)


# # Main program
# q = Queue()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# q.display()

# q.front()

# q.dequeue()
# q.display()

# q.dequeue()
# q.display()

# # TAsk 3(Binary search)
# arr = [10,20,30,40,50,60,70]    
# target = int(input("Enter the target element: "))

# low = 0
# high = len(arr) - 1 

# while low <= high:
#     mid = (low + high) // 2

#     if arr[mid] == target:
#         print("Element found at index:", mid)
#         break
#     elif arr[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
# else:
#     print("Element not found")    

# Take a string from user and print reversely

stack = []

#push
string = input("Enter a string: ")
for ch in string:
    stack.append(ch)

#display
print("Stack:",stack)

#Reverse
reverse = ""

#pop
while stack:
   reverse = reverse + stack.pop()

print("Reverse of string ",reverse)


#peak
# print("Top element:",stack[-1])

# if len(stack) == 0:
#     print("Stack is empty")
# else:
#     print("Stack is not empty") 