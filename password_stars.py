def main():
    """Ask the user for a password, check its length, and print asterisks."""
    MIN_LENGTH = 8  # Set the minimum length requirement

    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Prompt the user for a password and ensure it meets the minimum length."""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


if __name__ == "__main__":
    main()
