def encode(password):
    """
    Mutates the password argument by iterating over every numeric character and adding 3 to that digit.
    Returns the result after mutation.
    """
    return int("".join(str(int(digit)+3) for digit in password))


def decode(password):
    list_password = list(password)
    x = ""
    
    password2 = []
    for i in range(len(list_password)):
        i_tmp = str(int(list_password[i]) - 3)
        password2.append(i_tmp)
        x = "".join(password2)
    
    return x


def main():
    pass


if __name__ == "__main__":
    main()