l1=[10,12,14,16]
l2=[11,12,13,14]
# find common numbers
# o(t)-time complexity
# o(s)- space complexity
print("common numbers are")
for i in l1:
    for e in l2:
        if(i-e==0):
            
            print(i)
            
# print("COMMON ELEMENTS ARE")
# for i in l1:                           #MEATHPD 1
#     if i in l2:
#         print(i)

