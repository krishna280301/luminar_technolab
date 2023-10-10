actors=["Mohanlal","Mommotty","Jayasurya","Fahad Fasil","Tovino Thomas","vineeth"]
dileep=["Mohanlal","Jayasurya","Fahad Fasil"]

for i in actors:
    if(i not in dileep):
        dileep.append(i)
print(dileep)