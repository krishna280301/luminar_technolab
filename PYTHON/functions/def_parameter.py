def add(a,b):
    sum=a+b
    mul=a*b
    sub=a-b
    print(f"sum is {sum}")
    print(f"multiplied is is {mul}")
    print(f"subtracted is is {sub}")

num1=int(input("enter  first number "))
num2=int(input("enter second number "))
add(num1,num2)

num=int(input("enter a number "))
def oddeven(val):
    if(val%2==0):
        print("its even")
    else:
        print("its odd")
oddeven(num)

#print 3 numbers and find the largest
num1=int(input("enter first number "))
num2=int(input("enter second number "))
num3=int(input("enter third number "))
def largest(x,y,z):
    if(x>y) and (x>z):
        print(f"{x} is the largest")
    elif(y>x) and (y>z):
        print(f"{y} is the largest")
    else:
        print(f"{z} is the largest")
largest(num1,num2,num3)

#print consonents and vowels
str=input("enter a word ")
def one(s):
    v=0
    c=0
    for i in range(s):
        if(s[i] in ["a","e","i","o","u"]):
            v+=1
        else:
            c+=1
    print(f"vowels = {v}")
    print(f"consonents = {c}")
one(str)

return statement - a keyword inside function
def sum(a,b):
    s=a+b
    return s

print(sum(2,5))

# 1. find hcf using function
# 2. fund lcm using FileNotFoundError
# 3. chck given numis prime of not 
# 4. define a function that returns factorial of a number

           





