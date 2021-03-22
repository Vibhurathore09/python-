n = int(input())
i = 2
a=0
while i < n:
    if(n%i)==0:
        a=a+1
        break
    else:
        i=i+1
if(a!=0):
    print("Not Prime No")
else:
    print(" Prime")
