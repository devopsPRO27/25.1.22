class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def makeSound(self):
        print('maiking sound')

    def __str__(self):
        return f'animal name is {self.name}'

class Dog(Animal):
    def __init__(self,name,age,favbonzo):
        #self.name=name
        super().__init__(name,age)
        self.favbonzo=favbonzo
        #Animal.__init__(self,name)

    #override
    def makeSound(self):
        print("barking")
    #override
    def __str__(self):
        return super().__str__()+'  this is a dog'

an1=Animal('jojo the dog',24)
an2=Animal('haatol the cat',6)
dog1=Dog('rexy',9,'meat')

print(an1.name)
print(dog1.favbonzo)
dog1.makeSound()
an1.makeSound()
print(dog1)
#print(isinstance(an1,Animal))
#print(isinstance(an2,Animal))
#print(isinstance(dog1,Animal))
#print(isinstance(dog1,Dog))