s = str(input())
st = s.split()
end = str(input())
count = 0
for i in st:
    if i.endswith(end):
        count += 1
print("No of words ending with {0} are {1} ".format(end,count))