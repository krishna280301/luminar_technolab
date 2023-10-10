#1.k-m only in first place
#2.digit in second place and should be devisible by 3
#3.any number or charecter

from re import *
charecter=input("ENTER A CHARECTER ")
rule="[k-m][369][\w\W]*"
matcher=fullmatch(rule,charecter)
if(matcher==None):
    print(f"{charecter} IS INVALID")
else:
    print(f"{charecter} IS VALID")