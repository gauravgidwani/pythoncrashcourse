class Car:
    """docstring for Car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 99
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name.title())
    def update_odometer(self, mileage=0):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cannot!")
    def read_odometer(self):
        #self.odometer_reading = odometer_reading
        print(f"{self.odometer_reading} km")

tes = Car('merc benz', 'e250', 2019)
tes.get_descriptive_name()
tes.update_odometer(98)
tes.read_odometer()

class Battery():
    """docstring for Battery."""
    def __init__(self, battery_size):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"{self.battery_size} kWh")
    def get_range(self):
        range = self.battery_size*3.3*1.6
        print(f"This car can go {range} km on a full charge")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(0.25)

mytes = ElectricCar('tesla', 'model 3', 2020)
mytes.get_descriptive_name()
mytes.battery.describe_battery()
mytes.battery.get_range()
