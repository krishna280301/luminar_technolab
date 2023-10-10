#number of enquiries
enquiries=["django","testing","django","bigdata","django","aws","aws","django"]
e={}
for i in enquiries:
    if(i in e):
        e[i]+=1
    else:
        e[i]=1
print(e)