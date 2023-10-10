from re import *
# text="abaabababaabababaabaaba"
# pattern="ab"
# matcher=finditer(pattern,text)
# for i in matcher:
#     print(i.start(),i.group())


#"[a-z]" for all lowercase alphabets
#"[A-Z]" for all uppercase alphabets
#"[a-zA--Z]" for all alphabets
#"[0-9]" for all numbers
#"[a-zA-Z0-9]" for all alphabets and numbers
#"[^]" is given to exclude any set
#predefined charecters - "\d" for digits
                  #    - "\D" for excluding digits
                  #    - "\w" for alphabets and digits
                  #    - "\W" for special charecters



# text="abaAA#$@@BABba1233ab"
# pattern="[^a-zA-Z0-9]"
# matcher=finditer(pattern,text)
# for i in matcher:
#     print(i.start(),i.group())

text="#%(&@!)onetwothree1_23JOHNGAY"
pattern="[\W]"
matcher=finditer(pattern,text)
for i in matcher:
    print(i.start(),i.group())
    