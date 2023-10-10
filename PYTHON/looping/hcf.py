# num1=18
# num2=24
# for i in range(1,num2+1):
#     if(num1%i==0) and (num2%i==0):
#        hcf=i
# print(hcf)

# int=int(input("entre a number "))
# prime=True
# for i in range(2,int):
#     if(int%i==0):
#         prime=False
#         break
# print(prime)

# def hcf(num1,num2):
#     res=1
#     sm=num1 if num1<num2 else num2
#     for i in range(1,sm,+1):
#         if num1%i==0 and num2%i==0:
#             res=1
#             return res
# print(hcf(18,24))

# def lcm(num1,num2):
#     gcd=hcf(num1,num2)
#     res=(num1*num2)/gcd
#     return res
# print(lcm(18,24))

def lcm(n1,n2):
    max=n1 if(n1>n2) else n2
    lop=True
    while(lop):
        if(max%n1==00) and (max%n2==0):
            print(f"LCM of {n1} and {n2} is {max}")
            break
        else:
            max=max+1
lcm(30,25)



