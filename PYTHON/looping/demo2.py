num=int(input("enter the number "))
mult=1
while(num!=0):
    digit=num%10
    mult=mult*digit
    num=num//10
print(f"product is {mult}")