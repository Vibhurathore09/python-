yer = int(input())
if yer%4==0 and yer%100!=0 or yer%400==0:
    print("leap year")
else:
    print("Not leap year")
    
