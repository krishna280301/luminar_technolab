# #print the largest number
# num1
# num2
# num3

num1=int(input("ENTER FIRST NUMBER "))
num2=int(input("ENTER SECOND NUMBER "))
num3=int(input("ENTER THIRD NUMBER "))
if(num1>num2 and num1>num3):
    print(f"largest number is {num1}")
elif(num2>num1 and num2>num3):
    print(f"lagest number is {num2}")
else:
    print(f"largest number is {num3}")

if(num1>num2) and (num1>num3):
    print(f"largest number is {num1}")
elif(num2>num1) and (num2>num3):
    print(f"largest number is {num2}")
elif(num3>num2) and (num3>num1):
    print(f"largest number is {num3}")
elif(num1==num2) and (num1==num3):
    print(f"every number are equal")

if(num1>num2) and (num1>num3):
    print(f"largest number is {num1}")
    if(num2>num3):
        print(f"and the second largest number is {num2}")
    else:
        print(f"and the second largest number is {num3}")
elif(num2>num1) and (num2>num3):
    print(f"largest number is {num2}")
    if(num1>num3):
        print(f"and the second largest number is {num1}")
    else:
        print(f"and the second largest number is {num3}")
elif(num3>num2) and (num3>num1):
    print(f"largest number is {num3}")
    if(num1>num2):
        print(f"and the second largest number is {num1}")
    else:
        print(f"and the second largest number is {num2}")
elif(num1==num2) and (num1==num3):
    print(f"every number are equal")

if(num1>num2) and (num1>num3):
    if(num2>num3):
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
elif(num2>num1) and (num2>num3):
    if(num1>num3):
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
elif






