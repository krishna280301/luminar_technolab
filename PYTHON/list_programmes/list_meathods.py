users=["milana","krishnaprasad","johntd"]
users.append("gay") #used to add anything to a list
users.pop(2) #to remove anything in the string
print(users)
print(users.index("krishnaprasad")) #to find the position of anything in a string
print(users.count("milana")) #to know how many times anything has been used in a string

users.sort() #to display in alphabetical order
print(users)
users.sort(reverse=True) #to print in reverse order
print(users)
users.clear() #to empty the string 
print(users)

if("milana" in users): #to check weather the givin thing is present in the string
    print("present")
else:
    print("not present")

if("naveen" not in users):
    users.append("naveen")
print(users)
users.remove("milana") #to remove anything from a string
print(users)