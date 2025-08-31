import math

def calculate_circumference(radius):
    """
    Calculates the circumference of a circle.

    Args:
        radius (float or int): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number (integer or float).")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    circumference = 2 * math.pi * radius
    return circumference


try:
    user_radius = float(input("Enter the radius of the circle: "))
    circumference_result = calculate_circumference(user_radius)
    print(f"The circumference of the circle with radius {user_radius} is: {circumference_result:.2f}")
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")


fixed_radius = 5.0
fixed_circumference = calculate_circumference(fixed_radius)
print(f"The circumference of a circle with radius {fixed_radius} is: {fixed_circumference:.2f}")