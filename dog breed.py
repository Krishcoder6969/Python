class Dog:
    # Class variable: shared by all instances of the Dog class
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables: unique to each instance of the Dog class
        self.name = name
        self.breed = breed

    def display_details(self):
        """Displays the details of the dog."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}\n") # Accessing the class variable


# Create two instances of the Dog class with different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Poodle")

# Display the details of each dog
print("Details of Dog 1:")
dog1.display_details()

print("Details of Dog 2:")
dog2.display_details()