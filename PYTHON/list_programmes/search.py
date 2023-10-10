# to search for an element
print("SEARCHING A NUMBER")
lst=[12,13,14,15,16,17]
element=int(input("SEARCH - "))
i=0
found=False                            #normal search
while(i<len(lst)):
    current_value=lst[i]
    if(current_value==element):
        found=True
        break
    i+=1
print(found)


#binary search
lst=[10,13,12,14,16,15,17]
print(lst)
lst.sort()
element=int(input("SEARCH - "))
low=0
upp=len(lst)-1
while(low<=upp):
    mid=low+upp//2
    if(element==lst[mid]):
        found=True                      #binary search
        break
    elif(element<lst[mid]):
        upp=mid-1
    elif(element>lst[mid]):
        low=mid+1
print(found)
    


