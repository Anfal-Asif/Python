# Arr = [1,2,3,4,5]
# t = 5
# local = False

# for i in range(len(Arr)):
#     if Arr[i] == t:
#         local = True

# if local == True:
#     print("Value found")
# else:
#     print("Value not found")    


#Algo2

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# t = 5


# for i in range(len(l1)):
#     if l1[i] == t:
#         print("value found in array1")

#     else:
#         for j in range(len(l2)):
#            if l2[j] == t:
#              print("Value Found in array 2")


# # ALgo3
# A = [1,2,3]
# B = [1,2,3]

# for i in range(len(A)):
#     for j in range(len(B)):
#         if A[i] == B[j]:
#             print("True")
#         else:
#             print("False")    
           
# algo4
l1 = [1,2,3]
n = len(l1)

local = False

for i in range(n):
    for j in range(i+1 ,n):
        if l1[i] == l1[j]:
            local = True

if local:
    print("Array has duplicate elements")     
else:
    print("No duplicate element")         