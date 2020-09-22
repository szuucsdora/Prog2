import math

class Triangle:
    def __init__(self,p1,p2,p3=0):
        if p3==0:
            self.a=p1
            self.h=p2
        else:
            self.a=p1
            self.b=p2
            self.c=p3

    def area(self,):
        if hasattr(self,'c'):
            s=(self.a+self.b+self.c)/2
            area=(s*(s-self.a)*(s-self.b)+(s-self.c))**0.5
            return area
        else:
            return self.a*self.h/2

    def perimeter(self):
        if hasattr(self,'c'):
            return self.a+self.b+self.c
        else:
            return 'Nem lehet kiszámolni'


    def __str__(self):
        if hasattr(self,'c'):
            return 'A háromszög oldanalinak a hossza:({},{},{}).'.format(self.a,self.b,self.c)
        else:
            return 'A háromszög egyik oldala: {} és a hozzá tartozó magassága:{}'.format(self.a,self.h)


    def __add__(self, other):
        if isinstance(other,Triangle):
            return self.area() + other.area()
        if isinstance(other,int): #float,...
            return self.area() + other

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other,Triangle):
            return self.area() - other.area()
        if isinstance(other,int): #float,...
            return self.area() - other

    def __eq__(self, other):
        if isinstance(other,Triangle):
            return self.area() == other.area()


    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

T1=Triangle(3,4,5)
T2=Triangle(4,4)

# print(T1)
# print(T2)
#
# print(T1+5)
# print(T1+T2)
# print(T1-T2)
# print(T1<=T2)
# print(T1==T2)
# print(T1!=T2)

class Vector:
    origoX=0
    origoY=0

    def __init__(self,p1,p2):
        self.x=p1
        self.y=p2

    def __str__(self):
        return '<{},{}>'.format(self.x,self.y)

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        if isinstance(other,Vector):
            x=self.x+other.x
            y=self.y+other.y

        if isinstance(other,float):
            x = self.x + other
            y = self.y + other

        return self.__class__(x,y)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y

        if isinstance(other, float):
            x = self.x + other
            y = self.y + other

        self.x=x
        self.y=y
        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y

        if isinstance(other, float):
            x = self.x - other
            y = self.y - other

        return self.__class__(x, y)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y

        if isinstance(other, float):
            x = self.x * other
            y = self.y * other

        return self.__class__(x, y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.__abs__() == other.__abs()

    def __ne__(self, other):
        return self.__abs__() != other.__abs()

    def __gt__(self, other):
        return self.__abs__() > other.__abs()

    def __le__(self, other):
        return self.__abs__() <= other.__abs()

v1=Vector(1,2)
v2=Vector(3,4)

# print(v2)
# print(v1)
# v3=v1+v2
#
# print(v3)
# v3+=v3
# print(v3)
# print(v1*v2)

class ComplexNumbers:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __str__(self):
        return '({}+{}i)'.format(self.real,self.imag)

    def conjugate(self):
        return self.__class__(self.real,-self.imag)

    def argz(self):
        return math.atan(self.imag/self.real)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __add__(self, other):
        if isinstance(other,float):
            real_part=self.real+other
            imag_part=self.imag

        if isinstance(other,ComplexNumbers):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag

        return  self.__class__(real_part,imag_part)

    def __sub__(self, other):
        if isinstance(other, float):
            real_part = self.real - other
            imag_part = self.imag

        if isinstance(other, ComplexNumbers):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag

        return self.__class__(real_part, imag_part)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other,float):
            real_part = self.real - other
            imag_part = -self.imag

        return self.__class__(real_part,imag_part)

    def __mul__(self, other):
        if isinstance(other, float):
            real_part = self.real * other
            imag_part = self.imag * other

        if isinstance(other, ComplexNumbers):
            real_part = (self.real * other.real)-(self.imag*other.imag)
            imag_part = (self.real*other.imag + self.imag*other.real)

        return self.__class__(real_part, imag_part)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return (self.real == other.real ) and ( self.imag == other.imag)

    def __ne__(self, other):
        return (self.real != other.real) or (self.imag != other.imag)

c1=ComplexNumbers(3,4)
c2=ComplexNumbers(6,-2)
print(c2)

c3=c1*c2
print(c3)
print(c2!=c3)
print(c1.conjugate())
print(abs(c1))

