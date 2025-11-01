def calculate_tuple_product_loop(numbers_tuple):
    """
    Calculates the product of all numbers in a given tuple using a loop.

    Args:
        numbers_tuple: A tuple containing numerical values.

    Returns:
        The product of all numbers in the tuple.
    """
    product = 1
    for num in numbers_tuple:
        product *= num
    return product

# Example usage:
my_tuple = (2, 4, 6, 8)
result = calculate_tuple_product_loop(my_tuple)
print(f"The product of the numbers in {my_tuple} is: {result}")

another_tuple = (1, 3, 5, 7, 9)
result_2 = calculate_tuple_product_loop(another_tuple)
print(f"The product of the numbers in {another_tuple} is: {result_2}")