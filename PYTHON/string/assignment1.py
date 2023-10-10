# name="Python is a programming language"
# vowels=("a","e","i","o","u")
# words=name.split(" ")
# for w in words:
#     if w.casefold().startswith(vowels):
#         # print(w)


text="enter a sentance "
vowels=("a","e",'i',"o","u")
words=text.split(" ")
for i in words:
    if(i.casefold().startswith(vowels)):
        print(i)