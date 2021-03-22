n = input("enter the no - ")
s =len(n)
a= 0
for i in n:
    a += int(i)**s
if int(n) == a:
    print("Armstrong No")
else:
    print("Not Armstrong no")
