s = str(input())
lst = list(s)
for i in range(len(lst)):
    repeated = []
    for i in lst:
        if i in lst and  i not  in repeated:
            repeated.append(i)

print(repeated)