start=1
while(start<=5):
    print("hello world")
    start=start+1

int=0
while(int<=5):
    print(int)
    int=int+1

i=10
while(i>=1): #decriment
    print(i)
    i=i-1

e=1
while(i<=10): #incriment
    print(i)
    i=i+1

i=int(input("enter first number ")) #both user inputed
e=int(input("enter second number "))
while(i<=e):
    print(i)
    i=i+1

i=int(input("Enter a Number ")) #odd numbers
e=int(input("Enter another Number "))
while(i<=e):
    if(i%2!=0):
        print(i)
    i=i+1

i=int(input("enter first number"))
e=int(input("enter last number"))
while(i<=e):
    if(i%3==0) and (i%5==0):
        print(i)
    i=i+1

#sum of natural numbers upto 10

num=1
sum=0
while(num<=10):
    sum=sum+num
    num=num+1
print(sum)

# #SUM OF ALL ODD NUMBERS RANGE GIVEN BY USER
i=int(input("enter first number "))
e=int(input("enter last number "))
sum=0
while(i<=e):
    if(i%2!=0):
       sum=sum+i
    i=i+1
print(f"sum is {sum}")

a=int(input("enter another number "))
b=int(input("enter last number "))
c=0
while(a<=b):
    if(a%2==0):
        c=c+a
    a=a+1
print(f"sum is {c}")


#YOU ARE HAVING AN ARITHAMETIC SEQUENCE WITH A COMMON DIFFERENCE OF 6
#THE SEQUENCE IS STARTING WITH 56 FIND THE SUM OF FIRST 10 TERMS IN THIS SEQUENCE

num=1
while(num<=10):
    print(f"{num}*2={num*2}")
    num=num+1

num1=56
sum=0
while(num1):
    
num=int(input("enter first number "))
start=int(input("enter second number "))
f=1
while(num<=start):
    f=f*num
    num=num+1
print(f)

num=324
while(num!=0):
    digit=num%10
    print(digit , end="")
    num=num//10

num=324
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num=num//10
print(f"sum is {sum}")