class grandparent:
    def wealth(self):
        print("neha")
class parent(grandparent):
    def talent(self):
        print("is beautiful")
class child(parent):
    def girl(self):
        print("yes")
c=child()
c.talent()
c.wealth()
c.girl()



class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")

class Cow(Animal):
    def sound(self):
        print("Cow says Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()

