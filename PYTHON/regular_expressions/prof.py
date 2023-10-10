from re import *
phone_rule="[\d]{10}"
mail_rule="[a-z][\w\W]+[@]gmail[.]com"
phone_numbers=[]
mail_ids=[]
f=open("D:\\CODING\\LUMINAR TECHNOLAB\\luminar_projects\\regular_expressions\\data.txt",)
for line in f:
    words=line.rstrip("\n").split(" ")
    for i in words:
        p_match=fullmatch(phone_rule,i)
        g_match=fullmatch(mail_rule,i)
        if(p_match!=None):
            phone_numbers.append(i)
        elif(g_match!=None):
            mail_ids.append(i)
print(f"EMAIL IDS ARE {mail_ids}")
print(f"PHONE NUMBERS ARE {phone_numbers}")

