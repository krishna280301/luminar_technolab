# decoraotr is used to reduce redundancy and add feature
def swap(fn):
    def inside(n1,n2):
        if(n1<n2):
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inside

def smart_div(fun):
    def inner(n1,n2):
        if(n2==0):
            print("0 IS INDIVISIBLE")
            return
        return fun(n1,n2)
    return inner
@swap
def sub(n1,n2):
    return n1-n2
@swap
@smart_div                 #colling second decorator
def div(n1,n2):
    return n1/n2

print(f"SUM IS {sub(5,10)}")
print(f"DEVIDED AMOUNT IS {div(0,10)}")





