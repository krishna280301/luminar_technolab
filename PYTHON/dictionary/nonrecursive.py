
text="BABABABSBSBSABANUYDHBDFDFFT"
txt={}
for wc in text:
    if(wc in txt):
        txt[wc]+=1
    else:
        txt[wc]=1
for k,v in txt.items():
    if(v==1):
        print(k)
