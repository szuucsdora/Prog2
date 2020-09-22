import  numpy as np

class ParentClass(object):
    pass

class ChildClass(ParentClass):
    pass

# ch=ChildClass()
# c=ParentClass
#
# print(ChildClass.__bases__)
# print(ParentClass.__bases__)
# print(object.__bases__)
# print(ch.__class__)
# print(issubclass(ch.__class__,ParentClass))

class Polygon:
    def __init__(self,p1):
        self.n=p1
        self.sides=[0.0 for x in range(p1)]

    def inputSides(self):
        for i in range(0 , len(self.sides)):
            self.sides[i]=int(input('Írja be az {}. oldal hosszát'.format(i+1)))

    def printSides(self):
        for i in range(0, len(self.sides)):
            print('A {}. oldal hossza: {}'.format(i+1,self.sides[i]))

# p1=Polygon(6)
# print(p1.sides)
#
# p1.inputSides()
# p1.printSides()

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def getPerimeter(self):
        p=0
        for i in self.sides:
            p+=i
        return float(p)

    def getArea(self):

        s=self.getPerimeter()/2
        A=s
        for i in self.sides:
            A*=float(s-i)

        return A**0.5

# T1=Triangle()
#
# T1.inputSides()
# T1.printSides()
# print(T1.getPerimeter())
# print(T1.getArea())

class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount

    def withdrow(self,amount):
        self.balance-=amount

    def __str__(self):
        return 'A számla egynelege : {}'.format(self.balance)

class PreDeterminedMinAccount(BankAccount):
    def __init__(self,p1):
        BankAccount.__init__(self)
        self.minlimit=-p1

    def withdrow(self,amount):
        if self.balance-amount >= self.minlimit:
            super().withdrow(amount)
        else:
            print('Sajnálattal közöljük, hogy elérte a hitelkeretét.')

c=PreDeterminedMinAccount(100)
c0=BankAccount()
print(c.minlimit)
print(c0)

for i in range (1,15):
    if int(np.random.randint(0,2)) == 0:
        c.withdrow(int(np.random.randint(1,101)))
    else:
        c.deposit(int(np.random.randint(1, 101)))

    print(c)