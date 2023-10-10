# at least one uppercase
# at least one special charecter 
# mimimum 8 charecters

from re import *
password=input("ENTER YOUR PASSWORD - ")
condition="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}"
matcher=fullmatch(condition,password)
if(matcher==None):
    print("invalid")
else:
    print("valid")