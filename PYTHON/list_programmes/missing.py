one=[1,4,6,5,7,10]
one.sort()
# if(one[0!=1]):
#     print("1 is missing")
# else:

for i in range(0,len(one)-1):
       c=one[i]
       n=one[i+1]
       if(n-c!=1):
          print(c+1,"is missing")
        

