
# 
# # Question 4
# # IP   
# # Enter Array Size: 5
# # Enter Array: 95, 80, 953, 72, 4 
# #Enter Number of Digits :3  
# 
# 
# size = int(input("Enter Array Size: "))
# arr =[]
# for l in range(0,size):
#     inp =int(input("Enter Number: "))  
#     arr.append(inp)
# 
# 
# # arr = [95, 80, 953, 72, 4]
# digit= int(input("Enter Number of Digits"))
# lst = []
# for i in range(len(arr)):
#     if len(str(arr[i])) == digit:
#         lst.append(arr[i])
#     for j in range(i+1,len(arr)):
#         if len(str(arr[i])+str(arr[j]))== digit:
#             lst.append(int(str(arr[i])+str(arr[j])))
#             lst.append(int(str(arr[j])+str(arr[j])))
# num1 ,num2 = 0,0
# 
# for i in lst:
#     if i>num1:
#         num2=num1 
#         num1= i
#     elif i>num2:
#         num2 = i  
# 
# print(num2)

# Working
