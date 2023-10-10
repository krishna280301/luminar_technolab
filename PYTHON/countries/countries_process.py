from json import load                              #load is used to read a json file , loads is used to read a string json file
path="D:\\CODING\\LUMINAR TECHNOLAB\\luminar_projects\\countries\\countries.json"
with open(path,encoding="utf-8") as i:
    countires=load(i)                              #here the data is loaded into python file

#total countries
print(f"TOTAL COUNTIRES ARE {len(countires)}")     #total number of countires are printed

#priting name
c_names=[n.get("name") for n in countires]
# print(f"COUNTRY NAMES ARE {c_names}")

#print capital of china
cap_china=[cp.get("capital") for cp in countires if(cp.get("name")=="China")]
#print(f"CAPITAL OF CHINS IS {cap_china}")

#print country regions
region={r.get("region") for r in countires}
#print(f"ALL REGIONS {region}")

#print borders of India
in_br=[br.get("borders") for br in countires if(br.get("name")=="India")][0]
#print(f"INDIAN BORDERS ARE {in_br}")
nameof_br=[nc.get("name") for nc in countires if(nc.get("alpha3Code")) in in_br]
#print(f"BORDER COUNTRIES ARE {nameof_br}")

#print currency of india
cu_in=[ci.get("currencies") for ci in countires if(ci.get("name")=="India")][0][0]
# indian_curr=(i.get("name") for i in cu_in)   #wrong 
# print(cu_in.get("name"))
#print country with no currencies
no_currency=[nc.get("name") for nc in countires if("currencies") not in nc]
# print(f"COUNTRY WITH NO CURRENCY IS {no_currency}")

#print the most popular currency
country_currencies=[c for c in countires if("currencies") in c]
currency=[cu.get("currencies")[0].get("name") for cu in country_currencies]
total={}
for i in currency:
    if(i in total):
        total[i]+=1
    else:
        total[i]=1
print(max((v,k) for k,v in total.items()))

