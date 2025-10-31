def check_age():
    while True:
        try:
            age_input = input("Please enter your age: ")
            age = int(age_input)

            if age < 0 or age > 120:  # Assuming a realistic age range for validation
                print("Error: Age must be between 0 and 120.")
            else:
                print(f"You entered a valid age: {age}")
                if age % 2 == 0:
                    print("Your age is an even number.")
                else:
                    print("Your age is an odd number.")
                break  # Exit the loop if a valid age is entered

        except ValueError:
            print("Error: Invalid input. Please enter a whole number for your age.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Call the function to run the program
check_age()