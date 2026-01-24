class A:
    def __init__(self,a):
        self.a = a 
    def __lt__(self,other):
        if (self.a < other.a):
            return "ob1 is smaller than ob2"
        else:
            return "ob2 is smalleer than ob1"
    def __eq__(self,other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
        
ob1 = A(245)
ob2 = A(6767)
print (ob1 < ob2)

ob3 = A(292)
ob4 = A(292)
print (ob3 == ob4)