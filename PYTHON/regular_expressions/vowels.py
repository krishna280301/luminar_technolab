#print all consonents only
from re import *
text="goodmorning #sachin 009"
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)
for i in matcher:
    print(i.group())

