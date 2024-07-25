import sys


def encode(password):
    """
    Mutates the password argument by iterating over every numeric character and adding 3 to that digit.
    Returns the result after mutation.
    """
    return "".join(str(int(digit)+3) for digit in password)


def decode(password):
    list_password = list(password)
    x = ""
    
    password2 = []
    for i in range(len(list_password)):
        i_tmp = str(int(list_password[i]) - 3)
        password2.append(i_tmp)
        x = "".join(password2)
    
    return x


def show_menu_and_get_input():
    choice = 0
    while choice <= 0 or choice > 3:
        print("Menu")
        print("----------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit", end="\n\n")
        try:
            choice = int(input("Please enter an option: "))
        except ValueError:
            choice = 0
            print("Enter a valid menu choice.", end="\n\n")

    return choice


def main():
    current_password = ""
    while True:
        choice = show_menu_and_get_input()
        if choice == 1:
            password_entered = input("Please enter the password to encode: ")
            current_password = encode(password_entered)
            print("Your password has been encoded and stored!", end="\n\n")
        elif choice == 2:
            print(f"The encoded password is {current_password}, and the original password is {decode(current_password)}.")
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
