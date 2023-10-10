# add=lambda n1,n2:n1+n2
# subtract=lambda n1,n2:n1-n2
# cube=lambda n:n*n*n
# print(add(10,20))
# print(subtract(50,10))
# print(cube(5))

# sqaure=lambda n:n*n
# print(sqaure(2))

# max=lambda n1,n2:n1 if n1>n2 else n2
# print(max(10,20))

# # find the longest word
# text="hello hai goodmorning"
# words=text.split(" ")            #this is according to ASCII values
# longest=max(words)
# print(longest)

# text="hello hai goodmorning"
# words=text.split(" ") 
# longest=max(words,key=lambda w:len(w))
# print(longest)

# smallest=min(words,key=lambda w:len(w))
# print(smallest)

# sorting=sorted(words,reverse=True,key=lambda w:len(w))
# print(sorting)

# #collectionss 
# # list [] duplicates allowed , insertion order preserved , mutable
# # tuple () duplicates allowed , immutablee
# # set set() duplicates not allowed , insertion order not preserved


# text1="python is a simple software"
# words=text1.split(" ")
# longest=max(words,key=lambda i:len(i))
# shortet=min(words,key=lambda i:len(i))
# sorting=sorted(words,reverse=True, key=lambda i:len(i))
# print(f"longest word in '{text1}' is {longest}")
# print(f"shortest word in '{text1}' is {shortet}")
# print(sorting)

text="i love trangenders cum and go"
words=text.split(" ")
large=max(words,key=lambda i:len(i))
print(f"laargest word is {large}")