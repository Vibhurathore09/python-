n = input()
ln = len(n)
a = 0
i=0
while (i<ln):
    a += int(n[i])**ln
    i = i+1
if int(n) == a:
    print("armstrong")
else:
    print("Not armstrong")
    
