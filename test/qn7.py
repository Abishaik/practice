# a= int(input())
# 
# lst=[]
# 
# for i in range(a):
#     te = input()
#     lst.append(te)
# 
# dict ={
#     1:"one",
#     2:"two",
#     3:"three",
#     4:"four",
#     5:"five",
#     6:"six",
#     7:"seven",
#     8:"eight",
#     9:"nine",
#     10:"ten",
#     11:"eleven",
#     12:"twelve",
#     13:"thirteen",
#     14:"fourteen",
#     15:"fifteen",
#     16:"sixteen",
#     17:"seventeen",
#     18:"eighteen",
#     19:"nineteen",
#     20:"twenty",
#     30:"thirty",
#     40:""
#     }


a= int(input())
val= sorted(range(1,a+1),key=str)

print(val)