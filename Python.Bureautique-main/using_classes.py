class Circle:
    # Static variable
    PI = 3.141592653589793

    def __init__(self, radius):
        # Instance variable
        self.radius = radius

    # Instance method
    def get_perimiter(self):
        return 2*Circle.PI*self.radius

    @classmethod
    # Class method
    def get_perimeter_for_radius(cls, radius):
        return 2*cls.PI*radius

    @staticmethod
    # Static method
    def get_name():
        return "I am a Circle Class."


# Creating an instance of MyClass
circle = Circle(2)

# Accessing instance variable
print(circle.radius)
# Accessing static variable
print(Circle.PI)

# Calling instance method
# print(circle.get_perimiter())

# Calling class method
print(Circle.get_perimeter_for_radius(1))

# Calling static method
print(Circle.get_name())
