import string

CIPHER_CHARS = 'p7n0k8j9h6y5t4g3b2v1cxezmlaqwrsuiof'


def encrypt_password(password):
    """
    Encrypts a password using a simple substitution cipher and returns the encrypted password.
    """
    plain_chars = string.ascii_lowercase + string.digits
    password_dict = dict(zip(plain_chars, CIPHER_CHARS))
    encrypted_password = ''.join([password_dict.get(char, char) for char in password])
    return encrypted_password


def decrypt_password(encrypted_password):
    """
    Decrypts an encrypted password using a simple substitution cipher and returns the original password.
    """
    password_dict = dict(zip(CIPHER_CHARS, string.ascii_lowercase + string.digits))
    decrypted_password = ''.join([password_dict.get(char, char) for char in encrypted_password])
    return decrypted_password


def get_password_from_user():
    password = input("Enter password: ")
    password = password.lower()
    return password


# main loop
while True:
    # display options to the user
    print("Select an option:")
    print("1. Encrypt password")
    print("2. Decrypt password")
    print("3. Quit")

    # get the user's choice
    choice = input("> ")

    # perform the selected action
    if choice == '1':
        password = get_password_from_user()
        encrypted_password = encrypt_password(password)
        print(f"Encrypted password: {encrypted_password}")
    elif choice == '2':
        encrypted_password = get_password_from_user()
        decrypted_password = decrypt_password(encrypted_password)
        print(f"Decrypted password: {decrypted_password}")
    elif choice == '3':
        break
    else:
        print("Invalid choice")
