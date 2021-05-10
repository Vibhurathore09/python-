def find_len(s):
    c = 0
    for i in s:
        c = c + 1
    return c 
s = input("Enter your string")
print(find_len(s))