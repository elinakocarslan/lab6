# elina kocarslan

# encoder funtion checks each item in password and adds new decoded value to a list
def encoder(password):
    encoded_password = []
    for i in range(len(password)):
        encoded_num = int(password[i]) + 3
        encoded_password.append(str(encoded_num))
        encoded1_password = ''.join(encoded_password)
    return encoded1_password


def main():
    # while the code hasn't exited
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            user_password = (input("Please enter your password to encode: "))
            print(encoder(user_password))
            print("Your password has been encoded and stored!")
        elif user_option == 2:
            # once you do the decode()function you can put it here
            # decode(encoded_password):
            pass
        elif user_option == 3:
            exit()




if __name__ == '__main__':
    main()


