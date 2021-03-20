n = int(input())
k = bin(n).replace("0b","")
sk = str(k)
skl = len(sk)
for i in range (0,n+1):
    v = bin(i).replace("0b","")
    vk = str(v)
    vkl = len(vk)
    if(vkl<skl):
        for j in range(0,skl-vkl):
            print(" ",end="")
    print(v)
