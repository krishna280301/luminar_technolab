#opening another file
f=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\sample.txt","r")
# for line in f:
#     print(line)
words=[]
for line in f:
    words.append(line.rstrip("\n"))
print(words)

#with list comprehension
letters=[line.rstrip("\n") for line in f]
print(letters)
