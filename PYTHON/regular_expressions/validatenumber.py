from re import *
# phone_number=input("ENTER A PHONE NUMBER ")
# rule="\d{10}"
# matcher=fullmatch(rule,phone_number)
# if(matcher==None):
#     print(f"PHONE NUMBER {phone_number} IS INVALID")
# else:
#     print(f"PHONE NUMBER {phone_number} IS VALID")

variable=input("ENTER A VARIABLE ")
rule="[a-zA-Z][\w]*"
matcher=fullmatch(rule,variable)
if(matcher==None):
    print(f"VARIABLE {variable} IS INVALID")
else:
    print(f"VARIABLE {variable} IS VALID")