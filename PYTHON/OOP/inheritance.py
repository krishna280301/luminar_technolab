class parent:
    phone="SAMSUNG A 55"
    bike="PASSION PRO"

    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class child(parent):
    pass

obj=child()
obj.mobile()
obj.vehicle()