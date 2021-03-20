# Number of DAYS IN A MONTH
print('Program will print number of days in a given month')
flag = 1
month_days = int(input(("enter month (1-12)")))
if month_days == 2:
    year = int(input("enter year"))
    if year%4==0 and year%100!=0 or year%400==0:
        num_days = 29
    else:
        num_days = 28
elif month_days in {1,3,5,7,8,10,12}:
    num_days = 31
elif month_days in {4,6,9,11}:
    num_days = 30
else:
    print("enter valid month")
    flag = 0
if flag == 1:
    print("There are ",num_days, "days in ",month_days)

