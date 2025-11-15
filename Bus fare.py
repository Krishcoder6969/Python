class Vehicle:
    def __init__(self, name, max_speed, mileage, seating_capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        """Calculates the base fare for the vehicle."""
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        super().__init__(name, max_speed, mileage, seating_capacity)

    def calculate_fare(self):
        """Calculates the total fare for a bus, including a maintenance charge."""
        base_fare = super().calculate_fare()
        maintenance_charge = base_fare * 0.10  # 10% maintenance charge
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example Usage
school_bus = Bus("School Volvo", 180, 12, 50)
print(f"The total fare for the {school_bus.name} bus is: ${school_bus.calculate_fare():.2f}")

car = Vehicle("Sedan", 200, 15, 4)
print(f"The total fare for the {car.name} car is: ${car.calculate_fare():.2f}")