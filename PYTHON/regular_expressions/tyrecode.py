# 3 digit
# /
# 2digitR
# 2 digit
# /
# 2digit and alphabet

from re  import *
tyre_code=input("ENTER TYRE CODE - ")
rule="[\d]{3}[/][\d]{2}[R][\d]{2}[/][\d]{2}[A-Z]{1}"
matcher=fullmatch(rule,tyre_code)
if(matcher==None):
    print(f"TYRE CODE {tyre_code} IS INVALID")
else:
    print(f"TYRE CODE {tyre_code} IS VALID")