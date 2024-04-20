class animal:
    def sound(self):
        pass


class Dog(animal):
    def sound(self):
        return "woof!"


class Cat(animal):
    def sound(self):
        return "meow!"


class Bird(animal):
    def sound(self):
        return "tweet!"


class Hybrid(Dog, Cat, Bird):
    pass


hybrid = Hybrid()

print(hybrid.sound())