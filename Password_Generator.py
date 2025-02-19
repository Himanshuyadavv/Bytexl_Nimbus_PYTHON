import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    # Create a pool of characters to choose from
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase  # Uppercase letters (A-Z)
    if use_lower:
        characters += string.ascii_lowercase  # Lowercase letters (a-z)
    if use_digits:
        characters += string.digits  # Digits (0-9)
    if use_special:
        characters += string.punctuation  # Special characters

    # If no valid characters are selected, return an error message
    if not characters:
        return "At least one character type must be selected!"

    # Generate a random password from the available characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    print("===================================")
    print("This program will help you generate a strong password.")
    print("You can customize the length of the password and choose which character types to include.")
    print("\nA strong password typically includes the following characteristics:")
    print("- At least 12 characters long")
    print("- A mix of uppercase and lowercase letters")
    print("- Inclusion of digits (0-9)")
    print("- Special characters (e.g., !, @, #, $, etc.)")
    print("- Avoid easily guessable words or phrases (like your name, 'password', etc.)")

    # Get user input for password configuration
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        if length < 8:
            print("Password length should be at least 8 characters for better security.")
            return
    except ValueError:
        print("Invalid input for length. Please enter a valid number.")
        return

    print("\nNow, let's customize your password:")
    print("You can choose to include the following character types:")

    use_upper = input("Include uppercase letters? (y/n) [Recommended for stronger passwords]: ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n) [Recommended for readability]: ").lower() == 'y'
    use_digits = input("Include digits (0-9)? (y/n) [Useful for stronger passwords]: ").lower() == 'y'
    use_special = input("Include special characters (e.g., !, @, #, etc.)? (y/n) [Recommended for extra security]: ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)

    if isinstance(password, str):
        print("\nGenerated Password: ", password)
    else:
        print("\nError: ", password)

    print("\nPassword generation complete!")
    print("\nTips for a Strong Password:")
    print("- Use a password with at least 12 characters.")
    print("- Make sure to include uppercase and lowercase letters, numbers, and special characters.")
    print("- Avoid using easily guessable patterns, such as '1234', 'password', or your name.")
    print("- Change your password regularly and avoid reusing the same password across multiple sites.")
    print("- Consider using a password manager to securely store and generate strong passwords.")

    print("\nThank you for using the Password Generator. Stay safe online!")

if __name__ == "__main__":
    main()
