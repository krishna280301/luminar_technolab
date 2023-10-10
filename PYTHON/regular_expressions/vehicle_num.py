# first 2 uppercase alphabets
# then 2 digits
# then uppercase charecters minimum 1 and maximum 2
# last 4 digits

from re import *
vehicle_number=input("ENTER VEHICLE NUMBER - ")
rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"
matcher=fullmatch(rule,vehicle_number)
if(matcher==None):
    print(f"VEHICLE NUMBER {vehicle_number} IS INVALID")
else:
    print(f"VEHICLE NUMBER {vehicle_number} IS VALID")