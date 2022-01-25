class Person:
    def __init__(self,name,age,salary):
        self.__age=None
        self.__salary=None
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self):
        return f'Person  name ={self.name} , age={self.age}     salary{self.salary}'

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,v):
        if v> 5500:
            self.__salary=v

    @property
    def age(self): #getter
        return self.__age
    @age.setter
    def age(self,value):
        if value>0:
            self.__age=value


dana=Person('dana',55,14000)
ameer=Person('amer',-9,2500)
print(ameer)
print(dana)
print(dana.age)

dana.age=14
print(dana.age)

