from re import *
# + will print one or more occurance of a given element
# * zero or more occurence of an element
# a{1,2} means minimum 1 and maximum 2 a
text="aaabbbaaabbabababababababaabbbaababaaaaaaaaaaaaaaa"
pattern="a{1,2}"
matcher=finditer(pattern,text)
for i in matcher:
    print(i.start(),i.group())

#[a-z][a-zA-Z0-9]* - default variable declaration in python

