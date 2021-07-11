# Question 5 
# IP 12321 21123


def findAnswer(a,b):
    length = len(str(a))-1
    val =a%(10**length)
    ano =a//(10**length-1)
    final = (val*10)+ano
    count = 2
    if final ==b:
        return count 

    while final != a:
        val = final%(10**length)
        ano = final//(10**length-1)
        final =(val*10)+ano
        count+=1   
        if final ==b:
            return count
    return 0

print("Enter the Numbers")
a= int(input())
b= int(input())

ans = findAnswer(a,b)
if ans:
    print("True")
    print("Clockwise direction starting position wrt 1st integer "+str(ans))
    print("AntiClockwise direction starting position wrt 1nprintd integer "+str(findAnswer(b,a)))
else:
    print("False")
