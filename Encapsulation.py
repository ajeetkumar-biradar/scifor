class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car("Toyota", "Camry", 2020)

print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_car.odometer_reading)
my_car.odometer_reading = 100
print(my_car.odometer_reading)

my_car.odometer_reading += 50
print(my_car.odometer_reading)
