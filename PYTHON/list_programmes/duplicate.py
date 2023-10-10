one=[5,2,5,3]
 for i in one:
     if(one.count(i)>1):
         print(i)
         break

 one.sort()
 for i in range(0,len(one)-1):
     c=one[i]
     n=one[i+1]
     if(c==n):
         print(c)
