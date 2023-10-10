#counting the number of orders
orders=["vegmeals","fishmeals","vegmeals","fishmeals","vb","cb","bb","vb","cb","bb","bb","vb","fried_rice"]
order_count={}
for i in orders:
    if(i in order_count):
        order_count[i]+=1
    else:
        order_count[i]=1
print(order_count)

