#!/bin/python3
#Class 6 Python Script
#DJ Choi
#4/11/2022
#Writing python script to encrypt and decrypt



# Import Libraries
from cryptography.fernet import Fernet

# Declare Functions

#menu
def menu():
    choice = input("Options:\n[1] Encrypt a file\n[2] Decrypt a file\n[3] Encrypt a message\n[4] Decrypt a message\nEnter a number: ")

    if choice == '1':  
        filename = input("Enter filepath: ")
        encrypt(filename)

    elif choice == '2':
        filename = input("Enter filepath: ")
        decrypt(filename)

    elif choice == '3':
        message = input("Enter message: ")
        encrypt_message(message.encode())

    elif choice == '4':
        message = input("Enter message: ")
        decrypt_message(message.encode())

    else:
        print("Invalid choice. Please try again.")

#generates key and save it to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#load key
def load_key():
    return open("key.key", "rb").read()

#encrypt a message
def encrypt_message(message):
    write_key()
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print("Ciphertext is "+encrypted.decode('utf-8'))

#decrypt a message
def decrypt_message(message):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(message)
    print("Plaintext is "+str(decrypted.decode('utf-8')))

#encrypt file
def encrypt(filename):
    write_key()
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print("File encrypted")

#decrypt file
def decrypt(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File Decrypted")

# Main

menu()

#end





