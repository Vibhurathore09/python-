s = str(input())
words = list(s.split())
print(words)
small = large = len(words[1])
si = li = 0

for i in range(len(words)):
    
    if len(words[i]) >= large:
        large = len(words[i])
        li = i
    if len(words[i]) < small:
        small = len(words[i])
        si = i
print("smallest word is->",words[si])
print("largeest word is->",words[li])