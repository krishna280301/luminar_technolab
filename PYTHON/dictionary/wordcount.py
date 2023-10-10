#word count
text="hello hai hello hai hello"
t=text.split(" ")
wc={}
for i in t:
    if(i in wc):
        wc[i]+=1
    else:
        wc[i]=1
print(wc)
#[] used for list
#{} used in dictionary