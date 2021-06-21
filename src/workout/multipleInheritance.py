class A:
    def __init__(self):
        print("Class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B")

class C(A):
    def __init__(self):
        super().__init__()
        print("class C")

class D(B,C):
    def __init__(self):
        super().__init__()
        print("class D")


obj=D()
print(D.mro())