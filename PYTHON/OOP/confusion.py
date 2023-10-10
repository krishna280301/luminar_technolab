class mobile:
    def __init__(self,*args,**kwargs):
        self.name=kwargs.get("name")
        self.brand=kwargs.get("brand")
        self.display=kwargs.get("display")
    def dislay_details(self):
        print(self.name,self.brand,self.display)

class varient(mobile):
    price:int
    color:str
    
    def __init__(self, *args, **kwargs):
        self.price=kwargs.pop("price")
        self.color=kwargs.pop("color")
        print(self.price,self.color)
        super().__init__(kwargs)
    def display(self):
        super(self).display_details()
        print(self.price,self.color)


