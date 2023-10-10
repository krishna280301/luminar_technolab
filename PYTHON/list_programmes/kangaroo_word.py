#to find a kangaroo word
# print("CHECKING KANGAROO WORD")
# sourse=input("ENTER FIRST WORD - ")
# target=input("ENTER SECOND WORD - ")
# source_list=[]
# kangaroo=""
# for ch in sourse:
#     source_list.append(ch)
# for ch in target:
#     if(ch in source_list):
#         source_list.pop(source_list.index(ch))
#         kangaroo+=ch
# print(kangaroo==target)


# main=input("enter first word ")
# target=input("enter second word ")
# source_list=[]
# kang=""
# for i in main:
#     source_list.append(i)
# for i in target:
#     if(i in source_list):
#         source_list.pop(source_list.index(i))
#         kang+=i
# print(kang==target)


print("CHECKING KANGAROO WORD")
main=input("ENTER FIRST WORD - ")
taget=input("ENTER TARGET WORD - ")
source_list=[]
kangaroo=""
# for i in main:
#     source_list.append(i)
# for i in taget:
#     if(i in source_list):
#         source_list.pop(source_list.index(i))
#         kangaroo+=i
# print(kangaroo==taget)

for i in main:
    source_list.append(i)
for i in taget:
    if(i in source_list):
        source_list.pop(source_list.index(i))
        kangaroo+=i
print(kangaroo==taget)   