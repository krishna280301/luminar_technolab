items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
]

# print total number of products
# print all product names
# print all in stock product names
# print product names avaialble under rs 50
# print all product names avilable in ranage of 20 to 50

print(f"TOTAL NUMBER OF PRODUCTS ARE - {len(items)}")
print("NAME OF EACH PRODUCTS ARE")
for i in items:
    print(i.get("name"))

print("IN-STOCK PRODUCTS ARE")
for i in items:
    if(i.get("avl_qty"))>0:
        print(i.get("name"))

print("PRODUCTS AVAILABLE UNDER rs-50")
for i in items:
    if(i.get("price"))<=50:
        print(i.get("name"))

print("PRODUCTS AVAILABLE BETWEEN 20 and 50")
for i in items:
    if(i.get("price"))>=20 and i.get("price")<=50:
        print(i.get("name"))

# USING LIST COMPREHENSION
print(f"total number of producst are - {len(items)}")

all_products=[i.get("name") for i in items]
print(all_products)

in_stock=[i.get("name") for i in items if(i.get("avl_qty")>0)]
print(in_stock)

u_fifty=[a.get("name") for a in items if(a.get("price")<50)]
print(u_fifty)

rangeof=[a.get("name") for a in items if(a.get("price")>50 and a.get("price")<500)]
print(rangeof)

# price of specific product
name_p=[i.get("price") for i in items if(i.get("name")=="oreo")]
print(name_p)

# change price of oreo
oreo_data=[i for i in items if(i.get("name")=="oreo")].pop()
oreo_data["price"]=90
print(items)

#costly  and low cost product
costly=max(items,key=lambda i:i.get("price"))
low_cost=min(items,key=lambda i:i.get("price"))
print(f"COSTLY PRODUCT IS {costly}")
print(f"CHEAPEST PODUCT IS {low_cost}")
