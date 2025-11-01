def process_squares_by_parity():
    """
    Prompts the user for a number range, calculates the squares of numbers
    within that range, and then separates the squared values into lists
    of odd and even numbers.
    """
    while True:
        try:
            start_range = int(input("Enter the starting number of the range: "))
            end_range = int(input("Enter the ending number of the range: "))
            if start_range > end_range:
                print("Error: Starting number cannot be greater than the ending number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    squared_numbers = []
    for num in range(start_range, end_range + 1):
        squared_numbers.append(num ** 2)

    odd_squares = []
    even_squares = []

    for square in squared_numbers:
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print(f"\nOriginal numbers in the range [{start_range}, {end_range}]: {list(range(start_range, end_range + 1))}")
    print(f"List of squared numbers: {squared_numbers}")
    print(f"Odd squared values: {odd_squares}")
    print(f"Even squared values: {even_squares}")

# Call the function to execute the program
process_squares_by_parity()