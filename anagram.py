s1 =str(input())
s2 = str(input())
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")