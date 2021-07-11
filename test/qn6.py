#   1
#  11
#  121
# 1331
# 
# n= int(input())
# 
# for i in range(n):
#     
#     print("".join(map(str,str(11**i))))

# 2 nd method

def fact(n):
    factt =1
    for i in range(1,n+1):
        factt=factt*i
    return(factt)

n= int(input())
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(fact(i)//(fact(j)*fact(i-j)),end=" ")
    print()