class Car:
    def __init__(self, name):
        self._name = name  # use underscore to indicate "private"

    @property
    def name(self):
        """Getter for car name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for car name"""
        if not value:
            raise ValueError("Car name cannot be empty.")
        self._name = value

    def manufacturer(self):
        return self._name


# object
Car_obj = Car("Ford")

# Using the getter
print(Car_obj.name)

# Using the setter
Car_obj.name = "Toyota"
print(Car_obj.name)
