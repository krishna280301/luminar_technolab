# #CHECKING LEAP YEAR

# year=int(input("ENTER THE YEAR "))
# if(year%4==0):
#     print(f"{year} is LEAP YEAR")           #this is wrong
# else:
#     print(f"{year} is not a LEAP YEAR")

#case 1
#if the year is centuary year  that must be devisible by 400

# case 2
# if the year is not centuary year , thrn must be devided by 4 


year=int(input("ENTER THE YEAR "))
if(year%100==0 and year%400==0):
    print(f"{year} is a LEAP YEAR")
elif(year%100!=0 and year%4==0):
    print(f"{year} is a LEAP YEAR")
else:
    print(f"{year} is not a LEAP YEAR")