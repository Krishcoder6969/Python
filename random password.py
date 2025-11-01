import random
import string

def generate_random_password(length):
    """
    Generates a random password consisting of lowercase letters, uppercase letters, and numbers.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Define the characters to use in the password
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Ensure the password contains at least one of each required character type
    password_list = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]

    # Fill the remaining length with random characters from the combined set
    for _ in range(length - len(password_list)):
        password_list.append(random.choice(characters))

    # Shuffle the list to randomize the order of characters
    random.shuffle(password_list)

    # Join the list of characters to form the final password string
    password = "".join(password_list)
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length < 3:
            print("Warning: For a stronger password, consider a length of at least 3 to include all character types.")
            
        generated_password = generate_random_password(password_length)
        print(f"Generated Password: {generated_password}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")