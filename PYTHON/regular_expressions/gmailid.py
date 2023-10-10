# first 1-10 alphabets or numbers no special charecters
# last @gmail.com
# from re import *
# gmailid=input("ENTER YOUR GMAIL ID - ")
# rule="[a-z0-9]+[@]gmail[.]com"
# matcher=fullmatch(rule,gmailid)
# if(matcher==None):
#     print(f"GMAIL ID {gmailid} IS INVALID")
# else:
#     print(f"GMAIL ID {gmailid} IS VALID")

from re import *
gmail=input("enter your gmail id ")
rule="[a-z0-9]+[@]gmail[.]com"
matcher=fullmatch(rule,gmail)
if(matcher==None):
    print(f"{gmail} is invalid")
else:
    print(f"{gmail} is valid")

