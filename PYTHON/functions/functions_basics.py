# def add(n1,n2):
#     ans=n1+n2
#     return ans
# print(add(10,20))

# def cube(n):
#     res=n*n*n
#     return res
# print(cube(2))

# def max(n1,n2):
#     if(n1>n2):
#         return n1
#     else:
#         return n2
# print(max(111,101))

#          #or

# def max2(n,nn):
#     return n if(n>nn) else nn
# print(max2(100,101))

        

# def sub(m1,m2):
#     return(m1-m2)
# print(sub(10,8))

# def sub(n1,n2):
#     if(n1>n2):
#         return n1-n2
#     else:
#         return n2-n1
# print(sub(5,10))
# print(sub(10,5))

# #simplified 
# def subb(m1,m2):
#     return m1-m2 if(m1>m2) else m2-m1
# print(subb(100,1000))

# def oe(n):
#     return "Number is EVEN" if(n%2==0) else "Number is ODD"
# print(oe(9))

def hcf(n1,n2):
    res=1
    small=n1 if(n1<n2) else n2
    for i in range(1,small+1):
        if(n1%i==0) and (n2%i==0):
            res=i
    return res
n1=int(input("enter one number "))
n2=int(input("enter another number "))
print(hcf(n1,n2))