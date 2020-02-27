def doFinally():
    try:
        return 42
    finally:
        print("finally")

print(doFinally())



def returnStuff() -> int:
    return "a"

aap = returnStuff()

if(type(aap) == str):
    aap.start

print(returnStuff())

class Friet:
    def __init__(self, a):
        pass