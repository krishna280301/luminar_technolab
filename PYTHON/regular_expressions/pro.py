from json import load
path="D:\\CODING\\LUMINAR TECHNOLAB\\luminar_projects\\regular_expressions\\data.txt"
with open(path) as f:
    record=load(f)
print(record)