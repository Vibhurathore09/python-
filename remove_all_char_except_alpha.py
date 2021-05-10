s = str(input())
st = s.lower()
newstring = ''
valid = 'abcdefghijklmnopqrstuvwxyz'
for i in st:
    if i in valid:
        newstring = newstring + i
print(newstring)