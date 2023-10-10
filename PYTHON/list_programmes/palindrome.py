# text="madam"
# i=reversed(text)
# if(i==text):
#     print("is palindrome")
# else:
#     print("not palindrome")
# print(i)
##
text="malayalam"
count=len(text)-1
pal=""
for i in range(count,-1,-1):
    pal+=text[i]
print("palindrome" if text==pal else "not palindrome")

