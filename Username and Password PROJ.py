# If statements practice!
print("Starting program...\n")
print("Let's get an account created for you. First, make a username and password.\n")


def username_check(is_string):
    username = input("Enter your username (letters only): ")

    while is_string == False:

        if str.isalpha(username):
            print("Your username is", username)
            return True
#            print("Your username is", username, "\nIs this correct? (Y/N)")
#            verify = input("Confirm: ")

#            if verify == "Y" or "y":
#                print("Thank you! One moment...\n")
#                return True

#            else:
#                username.clear()
#                verify.clear()
#                username_check(False)

        else:
            print("Please type only letters. Try again.\n")
            username_check(False)


# def password_check(is_valid):
#    password = input("Enter your password (must contain a special character): ")

#    while is_valid == False:
#        if


username_check(False)
# password_check(False)
