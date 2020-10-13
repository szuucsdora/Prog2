class Author:
    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.book=[]

    def get_first_name(self):
        return self.first_name

    def get_second_name(self):
        return self.second_name

    def add_book(self,b):
        try:
            file=open(b,"r")
            for str in file:
                tmp=str.split(";")
                for i in range(5):

                    self.book.append(tmp[i])
        except FileNotFoundError:
            print('nem található a fajl.')

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __str__(self):
        return ('First name: {}, second name: {}.'.format(self.first_name,self.second_name))

    def __ge__(self, other):
        if self.first_name==other.first_name:
            return self.second_name > other.second_name
        else:
            return self.first_name > other.first_name

    def __lt__(self, other):
        if self.first_name==other.first_name:
            return self.second_name < other.second_name
        else:
            return self.first_name < other.first_name

    def printAuthor(self):
        print( str(self.first_name) + ' '+ str(self.second_name))




class Books:



    def __init__(self,title,date,price,first_name,second_name):
        self.title=title
        self.date=date
        self.price=price
        Author.__init__(self,first_name,second_name)


    def get_author(self):
        return Author.get_first_name()+' '+Author.get_second_name()

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_price(self):
        return self.price

    def __str__(self):
        return self.title + " | " + self.date + " | " + "  Price: " + self.price + "$ | Author: " + Books.get_author() + ":\n"

    def __ge__(self, other):
        if self.price==other.price:
            return self.title > other.title
        else:
            return self.price > other.price

    def __lt__(self, other):
        if self.price == other.price:
            return self.title < other.title
        else:
            return self.price < other.price


class Bookshop:
    def __init__(self,name,loc):
        self.name=name
        self.loc=loc
        self.book1=[]

    def inputBooks(self,filename):
        try:
            file = open(filename, "r")
            for str in file:
                tmp = str.split(";")
                tmp2 = tmp[1].split(' ')
                tmp3 = tmp[3].split(',')
                self.book1.append(tmp[0], tmp2, tmp[2], tmp3, tmp[4])


        except FileNotFoundError:
            print('nem található a fajl.')






