class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def __str__(self):
        str_print = f"{self.year} {self.make} {self.model}"
        return str_print

    def drive_forward(self, miles):
        self.odometer += float(miles)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_level = 100
    
    def print_battery_level(self):
        print(f"The current battery level is {self.battery_level}.")

    def drive_forward(self, miles):
        super().drive_forward(miles)
        self.battery_level -= (0.1 * miles)

if __name__ == "__main__":
    car1 = Car("Mazda", "Miata", 2023)
    car2 = ElectricCar("Tesla", "Model S", 2019)
    print(car1)
    print(car2)
    car2.print_battery_level()