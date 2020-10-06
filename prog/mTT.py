class Time:

    def __init__(self,hour,min):
        self.__hour = hour
        self.__min = min

    def getHour(self):
        return self.__hour

    def getMin(self):
        return self.__min

    def __str__(self):
        return self.__hour + ":" + self.__min

class City:

    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def __str__(self):
        return self.__name


class Station(City,Time):

    def __init__(self,name,hour,min):
        City.__init__(self,name)
        Time.__init__(self,hour,min)

    def __str__(self):
        return   Time.__str__(self) + "; " +City.__str__(self)

    def __ge__(self, other):
        if self.getHour() == other.getHour():
            if self.getMin() == other.getMin():
                return int(self.getName()) > int(other.getName())
            else:
                return int(self.getMin()) > int(other.getMin())
        else:
            return self.getHour() > other.getHour()

    def __lt__(self, other):
        if self.getHour() == other.getHour():
            return int(self.getMin()) < int(other.getMin())
        else:
            return int(self.getHour()) < int(other.getHour())


class IC:

    def __init__(self,id, name, arrival, dest):
        self.__id = id
        self.__name = name
        self.__arrival = arrival
        self.__dest = dest
        self.__stops = []

    def setArrival(self,newArrival):
        self.__arrival = newArrival

    def setDest(self,newDest):
        self.__dest = newDest

    def getArrival(self):
        return self.__arrival

    def getDest(self):
        return self.__dest

    def getName(self):
        return self.__name

    def getID(self):
        return self.__id

    def getStops(self):
        return self.__stops

    def inputStops(self,fileName):
        try:
            file = open(fileName,"r")
            for str in file:
                tmp = str.split(";")
                time = tmp[len(tmp)-1][:-1].split('.')
                self.__stops.append(Station(tmp[2],time[0],time[1]))
        except FileNotFoundError:
            print("A megadott fájl nem található!")

    def __str__(self):
        tmp = self.__name + "(" + self.__id + ")" + "  from: " + self.__arrival + "  to: " + self.__dest + ":\n"
        if len(self.__stops) == 0:
            return tmp + "Ismeretlen információ."
        else:
            self.__stops.sort()
            for i in self.__stops:
                tmp += i.__str__() + "\n"
            return tmp



#MAIN:
ic1 = IC('1652','Pava IC','Budapest-Nyugati','Nyiregyhaza')
ic1.inputStops('stops1652.txt')
ic2 = IC('617','Hajdu IC','Nyiregyhaza','Budapest-Nyugati')
ic2.inputStops('stops617.txt')
ic3 = IC('1023','Nyirseg IC','Tokaj','Debrecen')

print(ic1)
print(ic2)
print(ic3)
print()


ls = [ic1, ic2, ic3]
menetrend = dict([])

for ic in ls:
    for i in ic.getStops():
        if i.getName() not in menetrend:
            menetrend[i.getName()] = []
            menetrend[i.getName()] = [(Station(ic.getName(),i.getHour(),i.getMin()) , ic.getID()) ]
        else:
            menetrend[i.getName()].append((Station(ic.getName(),i.getHour(),i.getMin()) , ic.getID()))
            menetrend[i.getName()].sort()


key_ls = list(menetrend.keys())
key_ls.sort()
for k in key_ls:
    print(k + ":")
    for i in menetrend[k]:
        print(i[0].__str__() + ";(" + i[1] +")")