class BMW:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The {self.model} BMW's engine roars to life."

    def accelerate(self):
        return f"The {self.model} BMW smoothly accelerates."

    def stop_engine(self):
        return f"The {self.model} BMW's engine shuts down."

class Ferrari:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The {self.model} Ferrari's powerful engine ignites."

    def accelerate(self):
        return f"The {self.model} Ferrari rockets forward."

    def stop_engine(self):
        return f"The {self.model} Ferrari's engine falls silent."

def perform_car_actions(car):
    """
    This function demonstrates polymorphism by calling the same methods
    on different car objects without knowing their specific class type.
    """
    print(car.start_engine())
    print(car.accelerate())
    print(car.stop_engine())
    print("-" * 20)

# Create instances of BMW and Ferrari
bmw_m3 = BMW("M3")
ferrari_488 = Ferrari("488 GTB")

# Demonstrate polymorphism by calling the same function with different objects
perform_car_actions(bmw_m3)
perform_car_actions(ferrari_488)