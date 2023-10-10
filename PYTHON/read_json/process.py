from json import load
path="D:\\CODING\\LUMINAR TECHNOLAB\\luminar_projects\\read_json\\data.json"
with open(path) as f:
    record=load(f)
print(f"total records{record}")

f_name=[f.get("name") for f in record]
print(f_name)
top=max(record,key=lambda d:d.get("rating"))
print(f"most rated subject {top}")
print("python language")
pyfw=[i.get("name") for i in record if(i.get("language")=="python")]
print(pyfw)
print("backend subjects are")
back=[i.get("name") for i in record if(i.get("side")=="backend")]
print(back)

