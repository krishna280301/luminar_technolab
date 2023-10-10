#odd numbers between two numbers

print("DEVISIBLE BY 3")
num1=int(input("ENTER FIRST NUMBER "))
num2=int(input("ENTER LAST NUMBER "))
while(num1<=num2):
    if(num1%3==0):
        print(num1)
    num1=num1+1