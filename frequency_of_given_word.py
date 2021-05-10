s = str(input())
word = str(input()) #input word for which frequency is to be found
s1 = s.split()
lst = list(s1)
print(lst)
c = lst.count(word)
print(" word ({0}) is repeated {1} times".format(word,c))