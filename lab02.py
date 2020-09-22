# class Pont:
#     'Egy matematikai pont defje'
#
# p1=Pont()
#
# print(p1)
# p1.x=3.0
# p1.y=4.0
#
# print(p1.x)

class IntegerNum:
    'osztály leírása'
    def __init__(self,p1):
        self.number=p1

    def doubleNum(self):
        return self.number*2

    def squerNum(self):
        return self.number**2

    def pow(self,k):
        return self.number**k

    def abs(self):
        if self.number < 0:
            return self.number*(-1)
        elif  self.number > 0:
            return self.number
        else:
            return 0

n1=IntegerNum(6)
n2=IntegerNum(-8)
# print(n1.squerNum())
# print(n2.abs())

class Circle:
    pi=3.141592
    f=34
    def __init__(self,r):
        self.radius=IntegerNum(r)
        self.name='Kör'
        self.diameter=self.radius.doubleNum()

    def __str__(self):
        return '''A kör sugara: {}, kerülete: {},
         és területe {}'''.format(self.radius.number,self.getPerimeter(),self.getArea())

    def getArea(self):
        return self.radius.squerNum()*self.pi

    def getPerimeter(self):
        return self.radius.doubleNum()*self.pi

c1=Circle(5)
c2=Circle(3)

# print(c1.radius.number)
# print(c2)
# print(c1.__str__())

class Mystring:
    def __init__(self):
        self.str=''

    def getStr(self):
        self.str=input('Add meg a szöveget: ')

    def printString(self):
        print(self.str.upper())

# str1='Programozas'
# print(str1.upper())
#
# str2=Mystring()
# str2.getStr()
# str2.printString()

class SpecislElement0ifList:
    def __init__(self,ls):
        self.list=ls
        self.__length=len(ls)

    def getSumZeroSubLists(self):
        resLs=[]
        tmpLs=[]
        for i in range(0,self.__length):
            for j in range(i+1,self.__length):
                for k in range(j+1,self.__length):
                    tmpLs.append(self.list[i])
                    tmpLs.append(self.list[j])
                    tmpLs.append(self.list[k])
                    if sum(tmpLs)==0:
                        resLs.append(tmpLs)
                    tmpLs=[]
        return resLs



list1=SpecislElement0ifList([-25, -10, -7, -3, 2, 4, 8, 10])

print(list1.getSumZeroSubLists())
