class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery_capacity):
        super().__init__(registration, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration, max_speed, tank_volume):
        super().__init__(registration, max_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(120)
electric_car.drive(3)
gasoline_car.drive(3)
print(f"Electric Car (Registration: {electric_car.registration}) Distance: {electric_car.distance} km")
print(f"Gasoline Car (Registration: {gasoline_car.registration}) Distance: {gasoline_car.distance} km")
