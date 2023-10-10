studnet={"name":"KP","course":"python django","is_plaaced":True,"salary":24000}
for i in studnet.keys(): #to display all the keys
    print(i)

for e in studnet.values(): #to display  values
    print(e)

for i,e in studnet.items(): # to print key and value
    print(i,e)

print(studnet["course"]) #get can be used to coll a key and display the value
print(studnet.get("salary")) #using [] will print error if there is no key but .get("") will not print any error message

studnet.pop("name") #to remove a key value pair
print(studnet)

