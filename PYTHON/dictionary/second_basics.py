class hotel:
    items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10}

]
    # create() for add
    # retrieve() for taking 
    # distroy() for deleting
    # update() for updating
    # get()

    def create(self,*a,**k):
        self.items.append(k)
        return f"{k} created"
    def retrive(self,id=None,*a,**k):
        obj=[i for i in self.items if(i.get("id")==id)][0]
        return obj
    def delete(self,id=None,*a,**k):
        obj=[i for i in self.items if(i.get("id")==id)][0]
        self.items.remove(obj)
        return (f"{obj} has been removed")
    def update(self,id=None,*a,**k):
        obj=self.retrive(id=id)
        obj.update(k)
        return (f"{obj} has been updated")
obj=hotel()
# obj.create(id=106,name="BBQ",price=240)
# print(obj.retrive(id=102))
# print(obj.delete(id=100))
print(obj.update(id=102,name="chakka",price=100000000000  ))