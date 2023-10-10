n1=int(input("enter first number "))
n2=int(input("enter second number "))
if(n1==n2):
    print("both the numbers {n1} and {n2} areequal")
elif(n1>n2):
    print(f"{n1} is greater than {n2}")
else:
    print(f"{n2} is greater than {n1}")