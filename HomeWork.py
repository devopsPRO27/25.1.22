#1
#__init__(self,p1,p2,p3='hothaifa'):
#   self.p1=p1
#    self.p2=p2
#    self.p3=p3
#  p1.name?
#del p1.name

#2
#__init__(self)

#3

#4
#בנאי constructor

#5 __eq__()

#7
# str  prints the obj
# repr      for developers
# default
# print(obj)


#8
# returtn str

#9
#obj == obj
#__eq__
#obj + obj
#__add__

#10

class BankAccount:
    def __init__(self,id,fname,lname,balance ):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.balance=balance

    def __repr__(self):
        return f'BankAccount({self.id},{self.fname},\'{self.lname}\',{self.balance})'
    def __str__(self):
        return f'hello {self.fname} your balance is :{self.balance}'
    def __eq__(self, other):
        return self.balance == other.balance
        #if self.balance==other.balance: #True False
        #    return True
        #return False
    def __gt__(self, other):
        return self.balance>other.balance #true if the self balance greater than other balance
    def __add__(self, other):
        return self.balance + other.balance
    


acc=BankAccount(55,'hodi','zoubi',20)
print(acc)



















