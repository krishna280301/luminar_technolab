name="luminarl101"
print(name.casefold()) #convrting all to lowercase

n="john td"
print(n.capitalize()) #capitalising the first letter
print(n.count("a")) #calculating the number of times a particular alphabet repeats

print(name.index("a")) #print where the letter comes in case of number (position)
print(name.rstrip("l")) #to remove a letter either from left and right only
print(name.isalpha()) #to check weather the string has only alphabets space and special charetcers exclusive - space is not an alphabet
print(name.isdigit()) #to check weather the string is numbers only
print(name.isalnum()) #to check weather the string contains alphabet and digit

name="john is not a male kid"
word=(name.split(" "))
for w in word:
   print(w)  #to print all words seperately
text="curry"
word=sorted(text)
print(word)


