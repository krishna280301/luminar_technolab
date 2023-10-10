# text="aeiou"
# for ch in text:
#     if(ch in ["a","e","i","o","u"]): #in membership operator
#         print(ch)


text=input("enter text here - ")
vowel=0
conso=0
for ch in text:
    if(ch in ["a","e","i","o","u"]):
        vowel+=1
    else:
        conso+=1
print(f"total vowels are {vowel}")
print(f"total consonents are {conso}")
