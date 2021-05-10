import textwrap
s = str(input())
n = int(input())
words = []
#parts = [s[i:i+n] for i in range(0, len(s), n)]
for i in range(0,len(s),n):
    words[i] = s[i:i+n]
print(words)