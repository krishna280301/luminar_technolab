#OVERRIDING
class car:
    def start(self):
        print("KEY START")
    def break_type(self):
        print("DRUM BRAKES")
    def transmission(self):
        print("MANUAL GEARS")
class swift(car):
    pass
class audi6(car):
    def start(self):
        print("PUSH BUTTON START")
    def break_type(self):
        print("ABS")
    def transmission(self):
        print("8-SPEED AUTOMATIC")
print("SWIFT DETAILS")
car1=swift()
car1.start()
car1.break_type()
car1.transmission()

print("AUDI RS6 DETIALS")
car2=audi6()
car2.start()
car2.break_type()
car2.transmission()
