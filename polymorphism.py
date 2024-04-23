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


def make_sound(animal):
    print(animal.sound())


dog = Dog()
cat = Cat()
bird = Bird()

make_sound(dog)
make_sound(cat)
make_sound(bird)
