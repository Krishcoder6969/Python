import math

def calculate_trigonometric_values(angle_degrees):
    """
    Calculates the sine, cosine, and tangent of an angle given in degrees.

    Args:
        angle_degrees (float): The angle in degrees.

    Returns:
        tuple: A tuple containing the sine, cosine, and tangent values.
    """
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate sine, cosine, and tangent
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)

    return sine_value, cosine_value, tangent_value

# Example usage:
if __name__ == "__main__":
    try:
        user_angle_degrees = float(input("Enter an angle in degrees: "))

        sin_val, cos_val, tan_val = calculate_trigonometric_values(user_angle_degrees)

        print(f"\nFor an angle of {user_angle_degrees} degrees:")
        print(f"Sine: {sin_val:.4f}")
        print(f"Cosine: {cos_val:.4f}")
        print(f"Tangent: {tan_val:.4f}")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the angle.")
