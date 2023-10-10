items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},
]

# def add_items(*a,**k):
#     items.append(k)

# add_items(id=106,name="john",price=99)
# add_items(id=107,name="BBQ",price=200)
# # print(items)

# def retrieve_items(id=None,*a,**k):
#     obj=[i for i in items if(i.get("id")==id)]
#     return obj
# # print(retrieve_items(id=106))

# def delete_items(id=None,*i,**e):
#     obj=[i for i in items if(i.get("id")==id)][0]
#     items.remove(obj)
# delete_items(id=104)
# # print(items)

# def update_item(id=None,*ar,**kr):
#     obj=[i for i in items if(i.get("id")==id)][0]
#     obj.update(kr)
# update_item(id=102,name="stfu")
# print(retrieve_items(id=102))

def add_items(*a,**k):
    items.append(k)
add_items(id=110,name="saliva",price=1000)
# print(items)

def retreve_items(id=None,*a,**k):
    obj=[i for i in items if(i.get("id")==id)]
    return obj
# print(retreve_items(id=110))

def delete_itesm(id=None, *a,**k):
    obj=[i for i in items if(i.get("id")==id)][0]
    items.remove(obj)
delete_itesm(id=101)
# print(items)
