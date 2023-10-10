lst=[2,3,5,7]
sum=9
for i in range(0,len(lst)-1):
    for e in range(i+1):
        current=lst[i]+lst[e]
        if(current==sum):
            print(lst[i],lst[e])

# sum=9
# for i in range(0,len(lst)-1):
#     for e in range(i+1):
#         answer=lst[i]+lst[e]
#     if(sum==answer):
#             print(lst[i],lst[e])