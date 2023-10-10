# while True:
#     try:
#         x=int(input("ENTER A NUMBER "))
#         y=int(input("ENTER NEXT NUMBER "))
#         z=x/y
#         print(f"{x} DEVIDED BY {y} IS {z}")
#     except ValueError:
#         print("PLEASE ENTER A VALID NUMBER")
#     except TypeError:
#         print("PLEASE ENTER CURRECT VALUE")
#     except ZeroDivisionError:
#         print("ZERO CANNOT BE DEVIDED")
#     finally:
#         print("FUCK YOU")

while True:
    try:                                      # to run this code
        x=int(input("ENTER A NUMBER "))
        if(x%2==0):
            print(f"{x} IS AN EVEN NUMBER")
        else:
            print(f"{x} IS ODD NUMBER")
    except TypeError:                         # execute this code when there is an exception
        print("ENTER CURRECT VALUE")
    except ValueError:
        print("ENTER VALID NUMBER")
    finally:
        print("DAMN BRO")