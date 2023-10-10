from json import load
path="D:\\CODING\\LUMINAR TECHNOLAB\\luminar_projects\\PYTHON\\countries\\countries.json"
with open(path,encoding="utf-8") as i:
    counteis=load(i)

print(f"total countries are {len(counteis)}")