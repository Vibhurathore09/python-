s1 = str(input())
s2 = str(input())
l1 = list(s1)
l2 = list(s2)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] in l2[j]:
            l1.remove(l1[i])
print(str(l1))
