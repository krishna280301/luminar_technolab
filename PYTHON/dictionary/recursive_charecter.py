text="BABAASAC"
first={}
for i in text:
    if(i in first):
        print(f"first recurside letter is {i}")
        break
    else:
        first[i]=1
wc={}

second=[]
for i in text:
    if(i in wc):
        second.append(i)
    else:
        wc[i]=1
print(f"second recursiv letter is {second[1]}")

non_recu={}
for i in text:
    if(i in non_recu):
        non_recu[i]+=1
    else:
        non_recu[i]=1
for k,v in non_recu.items():
    if(v==1):
        print(f"non recursive letter is {k}")
