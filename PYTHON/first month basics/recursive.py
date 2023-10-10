#recursivecharecter
text="abaccbda"
first={}
for i in text:
    if(i in first):
        print(f"{i} is the first recursive charecter")
        break
    else:
        first[i]=1
wc={}
second=[]
for e in text:
    if(e in wc):
        second.append(e)
    else:
        wc[i]=1
print(f"{second[1]} is the second recursive charecter")

dup={}
for i in text:
    if(i in dup):
        dup[i]+=1
    else:
        dup[i]=1
for k,v in dup.items():
    if(v==1):
        print(f"{k} is the non recursive charecter")