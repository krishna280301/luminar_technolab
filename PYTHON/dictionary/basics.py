mobile={"brand":"SAMSUNG","model":"S22 ULTRA","price":60000,"special feature":"100X ZOOM LENS","offer":10000}
print(mobile["brand"])
print(mobile["model"])
print(mobile["price"])
print(mobile["special feature"])

#add "display":"amoled"
mobile["display"]="AMOLED"
mobile["storage"]="524GB"
print(mobile)

#to check if any key in a dictionary
if("offer" in mobile):
     print("offer is present")
else:
     print("offer is not present")

#to add offer amount
if("offer" in mobile):
    mobile["offer"]+=2000
else:
    mobile["offer"]=2000
print(mobile)
