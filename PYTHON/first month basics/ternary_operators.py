num=90
print("+ve" if num>0 else "-ve")
print("even" if num%2==0 else "odd")

num1=10
num2=20
print(num1 if num1>num2 else num2)

num=int(input("enter a number "))
print(num+1 if num>5 else num-1)

num1=int(input("enter first number "))
num2=int(input("enter second number "))
print(num1-num2 if num1>num2 else num2-num1)

num=int(input("enter a number "))
print("+ve" if num>0 else "-ve" if num<0 else "zero")

num=int(input("enter a number "))
print(num+1 if num>5 else num-1 if num<5 else 5)