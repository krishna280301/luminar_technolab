# first 3 charecters must be upper case random alphabets
# 4th place must be an alphabet(PCFHTA)
# 5th place any random uppercase alphabet
# then 4 digit
# last one alphabet 

# from re import *
# pan_number=input("ENTER PAN CARD NUMBER HERE - ")
# rule="[A-Z]{3}[PCFHTA]{1}[A-Z][\d]{4}[A-Z]{1}"
# matcher=fullmatch(rule,pan_number)
# if(matcher==None):
#     print(f"PAN NUMBER {pan_number} IS INVALID")
# else:
#     print(f"PAN NUMBER {pan_number} IS VALID")



from re import *
pan=input("enter pan number ")
rule="[A-Z]{3}[PCFHTA]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(rule,pan)
if(matcher==None):
    print(f"{pan} is invalid")
else:
    print(f"{pan} is valid")