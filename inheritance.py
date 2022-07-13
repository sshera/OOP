from tkinter.font import names


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Fuzzy", 5)
# p.show()
c = Cat("Fluffy", 7, "orange")
c.show()
d = Dog("Rex", 2)
# d.show()
f = Fish("Bubbles", 10)
# p.speak()
# c.speak()
# d.speak()
# f.speak()
