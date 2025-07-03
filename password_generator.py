#Task - 3 Password Generator 

import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    """Generate a password using selected character types."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    char_sets = []
    password_chars = []

    if use_lower:
        char_sets.append(string.ascii_lowercase)
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_upper:
        char_sets.append(string.ascii_uppercase)
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        char_sets.append(string.digits)
        password_chars.append(random.choice(string.digits))
    if use_special:
        char_sets.append(string.punctuation)
        password_chars.append(random.choice(string.punctuation))

    if not char_sets:
        raise ValueError("You must select at least one type of character.")

    all_chars = ''.join(char_sets)

    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_chars, k=remaining_length)

    random.shuffle(password_chars)

    return ''.join(password_chars)

def ask_yes_no(prompt):
    """Helper to ask yes/no questions."""
    while True:
        choice = input(prompt + " (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print("Please enter 'yes' or 'no'.")

def main():
    print("----------------------------------------------")
    print("--------------Password Generator--------------")
    print("----------------------------------------------")
    try:
        length_input = input("Enter the password length (minimum 4): ").strip()
        if not length_input.isdigit():
            raise ValueError("Password length must be a number.")
        length = int(length_input)

        use_lower = ask_yes_no("\nInclude Lowercase letters?")
        use_upper = ask_yes_no("Include Uppercase letters?")
        use_digits = ask_yes_no("Include Digits?")
        use_special = ask_yes_no("Include Special Characters?")
        
        print("\n-----------------------------------------------")

        password = generate_password(length, use_lower, use_upper, use_digits, use_special)
        print(f"           Generated Password is: {password}")
        print("-----------------------------------------------")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
