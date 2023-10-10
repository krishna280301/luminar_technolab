expenses=[12000,13000,14000,11000,25000,28000,21000]
# print(f"MARCH EXPENCE IS {expenses[2]}")

# print("ALL EXPENCES ARE")
print("EXPENCES GREATER THAN 16000 ARE ")
for i in expenses:
    if(i>16000):
       print(i)

# max=0
# for e in expenses:
#     if(e>max):
#         max=e
# print(f"THE MHIGHEST EXPENCE IS {max}")

# min=expenses[0]
# for a in expenses:
#     if(a<min):
#         min=a
# print(f"SMALLEST EXPENCE IS {min}")
# #important functions
# # sorted
# # min
# # max
# # sum
min=min(expenses)
max=max(expenses)
asc=sorted(expenses)
des=sorted(expenses,reverse=True)

print(f"MINIMUM EXPENCE IS {min}")
print(f"MAXIMUM EXPENCE IS {max}")
print(f"ASCENDING ORDER IS {asc}")
print(f"DECENDING ORDER IS {des}")
