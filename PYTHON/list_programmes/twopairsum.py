# one=[2,3,4,5]
# for i in range(0,len(one)):
#     for j in range(i+1,len(one)):  #complex meathod  
#         if(one[i]+one[j]==7):
#             break
#     print(one[i],one[j])
#     break
##

# one=[2,3,4,5]
# sum=7
# one.sort()
# low=0
# upp=len(one)-1
# while(low<upp):
#     csum=one[low]+one[upp]
#     if(csum==sum):
#         print(f"pairs are {one[low]} and {one[upp]}")
#         break
#     elif(csum<sum):
#         low+=1
#     else:
#         upp-=1

# lst=[2,3,4,5]
# sum=7
# lst.sort
# low=0
# upp=len(lst)-1
# while(low<upp):
#     csum=lst[low]+lst[upp]
#     if(csum==sum):
#         print(f"pairs are {lst[low]} and {lst[upp]}")
#         break
#     elif(csum<sum):
#         low+=1
#     else:
#         upp-=1


# numbers=[3,5,4,6]
# sum=9
# numbers.sort
# lwr=0
# upr=len(numbers)-1
# while(lwr<upr):
#     nsum=numbers[lwr]+numbers[upr]
#     if(nsum==sum):
#         print(f"pairs are {numbers[lwr]} and {numbers[upr]}")
#         break
#     elif(nsum<sum):
#         lwr+=1
#     else:
#         upr-=1

numbers=[1,2,3,4]
sum=5
numbers.sort
low=0
upp=len(numbers)-1
while(low<upp):
    nsum=numbers[low]+numbers[upp]
    if(nsum==sum):
        print(numbers[low],numbers[upp])
        break
    elif(nsum<sum):
        numbers[low]+=1
    else:
        numbers[upp]-=1