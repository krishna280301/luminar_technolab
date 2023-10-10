#variable length argument meathod - means there is no particular count 
# * - accept as tuple
# * - accept as dictionary and have more clarity
# def product(*ken):
#     result=1
#     for i in ken:
#         result*=i
#     print(result)

# product(1,2,3,4,5)
# product(3,5,6,7)

# def greet(*kp):
    # print(f"{kp[0]} app user {kp[1]} ")



#**
# def greetings(**kpcs):
    # print(f"")

def dispatch_order(**kwargs):
    print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')} {kwargs.get('item')} is {kwargs.get('status')}")

dispatch_order(item="ucb shirt", code="123bk", status="delivered", name="vijay")
