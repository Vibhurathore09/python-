s = str(input("Enter string"))
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
print(reverse(s))