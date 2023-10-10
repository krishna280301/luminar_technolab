# class p1:
#     def m1(self):
#         print("JOHN")
# class p2:
#     def m2(self):
#         print("IS")
# class child(p1,p2):
#     def m3(self):
#         print("GAY")

# obj=child()
# obj.m1()
# obj.m2()
# obj.m3()

#in python multiple inheritance is in order wise

class p1:
    def m1(self):
        print("JOHN")
class p2:
    def m1(self):
        print("IS")
class child(p2,p1):
    def m3(self):
        print("GAY")

obj=child()
obj.m1()
# obj.m2()
# obj.m3()