# elina kocarslan

# encoder funtion checks each item in password and adds new decoded value to a list
def encoder(password):
    encoded_password = []
    for i in range(len(password)):
        encoded_num = int(password[i]) + 3
        encoded_password.append(str(encoded_num))
        encoded1_password = ''.join(encoded_password)
    return encoded1_password

def decoder(password):
    #works
    decoded_password = []
    acc_decoded_pass = []
    for i in range(len(password)):
        decoded_num = int(password[i])-3
        decoded_password.append(str(decoded_num))
        acc_decoded_pass = ''.join((decoded_password))
    return acc_decoded_pass

def main():
    # while the code hasn't exited
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            user_password = (input("Please enter your password to encode: "))
            encoded_password = encoder(user_password)
            # print(encoder(user_password))
            print("Your password has been encoded and stored!")
        elif user_option == 2:
            # once you do the decode()function you can put it here
            # decode(encoded_password):
            pass
        elif user_option == 3:
            exit()




if __name__ == '__main__':
    main()


