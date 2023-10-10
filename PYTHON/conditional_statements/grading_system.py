# #grading system
# >80 = A
# >70 = B+
# >60 = B
# >50 = C
# >40 = C+
# >30 = D+
# <30 = FAIL 
#with if
str="GRADING SYSTEM"
print(str)
m=int(input("ENTER YOUR MARKS "))
if(m>=80):
    print(f"You have A grade")
if(m<80 and m>=70):
    print(f"You have B+ grade")
if(m<70 and m>=60):
    print(f"You have B grade")
if(m<60 and m>=50):
    print(f"You have C+ grade")
if(m<50 and m>=40):
    print(f"You have C grade")
if(m<40 and m>=30):
    print(f"You have D+ grade")
if(m<30):
    print(f"YOU HAVE FAILED")

# with elif

m=int(input("ENTER YOUR MARKS "))
if(m>=80):
    print(f"You have A grade")
elif(m<80 and m>=70):
    print(f"You have B+ grade")
elif(m<70 and m>=60):
    print(f"You have B grade")
elif(m<60 and m>=50):
    print(f"You have C+ grade")
elif(m<50 and m>=40):
    print(f"You have C grade")
elif(m<40 and m>=30):
    print(f"You have D+ grade")
else:
    print(f"YOU HAVE FAILED")



    
