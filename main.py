def encode(password):
    """
    Mutates the password argument by iterating over every numeric character and adding 3 to that digit.
    Returns the result after mutation.
    """
    return int("".join(str(int(digit)+3) for digit in password))


def main():
    pass


if __name__ == "__main__":
    main()