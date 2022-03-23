print("This is a calculator powered by TMath Module by Trevlin Morris")
print("Avaliable commands are:\nDiv\nMult\nAdd\nSub\nRound\nCompare")
def Div():
    A = float(input())
    B = float(input())
    C = A / B
    print(C)
def Mult():
    A = float(input())
    B = float(input())
    C = A * B
    print(C)
def Add():
    A = float(input())
    B = float(input())
    C = A + B
    print(C)
def Sub():
    A = float(input())
    B = float(input())
    C = A - B
    print(C)
def Round():
    A = float(input())
    X = round(A)
    print(X)
def Compare():
    A = float(input())
    B = float(input())
    if A > B:
        print("A is more than B")
    else:
        print("B is more than A")
def NoFunc():
    print("This is a function just for testing\nThis has no use")