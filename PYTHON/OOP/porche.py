class car:
    elements=["GT3RS","CAYMAN"]
    def names(self):
        return self.elements

class porche(car):
    def names(self):
        self.m=super().names()
        self.m.append("TURBO S")
        return self.m

brand=porche()
print(brand.names())