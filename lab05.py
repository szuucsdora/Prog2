# class A:
#     def m(self):
#         print('Az A m metódusa')
#
#
# class B(A):
#     def m(self):
#         print('Az B m metódusa')
#
#
# class C(A):
#     def m(self):
#         print('Az C m metódusa')
#
# class D(B,C):
#     pass
#
# x=D()
# x.m()

class Clock:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds

    def set(self,hours,minutes,seconds=0):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds

    def tick(self):
        'Az idő 1 másodperccel előre lép.'

        if self.__seconds==59:
            self.__seconds=0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 59:
                    self.__hours = 0

                else:
                    self.__hours +=1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

    def display(self):
        print("%d:%d:%d"%(self.__hours,self.__minutes,self.__seconds))

    def __str__(self):
        return ("%2d:%2d:%2d"%(self.__hours,self.__minutes,self.__seconds))

    def getora(self):
        return [self.__hours,self.__minutes,self.__seconds]

# ora=Clock()
# print(ora)
# ora.set(14,9,3)
# print(ora)
# # for i in range(100):
# #     ora.tick()
# #     print(ora)
# ora.display()

class Calendar:
    months=(31,28,31,30,31,30,31,31,30,31,30,31)
    def __init__(self,day=1,month=1,year=1900):
        self.__day=day
        self.__month=month
        self.__year=year

    def leapyear(self,y):
        if y%4:
            #nem szökőév
            return 0
        else:
            if y%100:
                return 1
            else:
                if y%400:
                    return 0
                else:
                    return 1

    def set(self,day,month,year):
        self.__day=day
        self.__month=month
        self.__year=year

    def get(self):
        return (self,self.__day,self.__month,self.__year)

    def advance(self):
        months=Calendar.months
        max_days=months[self.__month-1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)

        if self.__day == max_days:
            self.__day = 1

            if self.__month == 12:
                self.__month = 1
                self.__year+=1
            else:
                self.__month+=1
        else:
            self.__day+=1

    def __str__(self):
        return str(self.__day) + "/" + str(self.__month) + "/" + str(self.__year)

# x=Calendar(1,1,2000)
# for i in range(60):
#     x.advance()
#     print(x)
#
#

class CalendarClock(Clock,Calendar):
    def __init__(self,day,month,year,hours=0,minutes=0,seconds=0):
        Calendar.__init__(self,day,month,year)
        Clock.__init__(self,hours,minutes,seconds)

    def __str__(self):
        return Calendar.__str__(self) + ","+ Clock.__str__(self)

y=CalendarClock(7,6,1995,12,34,25)
print(y)

for i in range(5*365*86400):
    y.tick()
    if y.getora() == [23,59,59]:
        y.advance()
    print(y)