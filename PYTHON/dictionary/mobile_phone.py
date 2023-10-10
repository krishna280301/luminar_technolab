mobile_phones=[{"id":1,"name":"SAMSUNG S22","price":120000},
]
# #adding items
# def add_items(*args,**kwargs):
#     mobile_phones.append(kwargs)
# add_items(id=6,name="1+ NORD",price=40000)
# add_items(id=7,name="REALMI ONE",price=10000)
# add_items(id=8,name="ASUS ROGPHONE",price=50000)
# # print(mobile_phones)

# #selecting particular phone (RETRIVE ITEMS)
# def retrive_items(id=None,*a,**k):
#     item=[i for i in mobile_phones if(i.get("id")==id)]
#     return item
# # print(retrive_items(id=3))
# # print(retrive_items(id=5))

# #delete or remove items
# def delete_item(id=None,*a,**k):
#     item=[i for i in mobile_phones if(i.get("id")==id)][0]
#     mobile_phones.remove(item)
# delete_item(id=1)
# delete_item(id=2)
# delete_item(id=3)
# # print(mobile_phones)

# #updating or modifying items
# def update_item(id=None,*a,**k):
#     item=[i for i in mobile_phones if(i.get("id")==id)][0]
#     item.update(k)
# update_item(id=5,price=6999)
# # print(retrive_items(id=5))

def add_items(*a,**k):
    mobile_phones.append(k)
add_items(id=10,name="kus")
# print(mobile_phones)

def retreve_items(id=None, *a, **k):
    items=[i for i in mobile_phones if(i.get("id")==id)]
    return items
# print(retreve_items(id=1))

def delete_items(id=None,*a,**k):
    items=[i for i in mobile_phones if(i.get("id")==id)][0]
    mobile_phones.remove(items)
delete_items(id=1)
# print(mobile_phones)

def update_items(id=None,*a,**k):
    items=[i for i in mobile_phones if(i.get("id")==id)][0]
    items.update(k)
update_items(id=1,name="sala")
print(retreve_items(id=1))