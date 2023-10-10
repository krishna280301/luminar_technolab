def decor1(f):
    def inside():
        x=f()
        return x*x
    return inside
def decor2(f):
    def inside():
        x=f()
        return 2*x
    return inside
@decor1
@decor2
def num():
    return 10
print(num())


def word():
    return 