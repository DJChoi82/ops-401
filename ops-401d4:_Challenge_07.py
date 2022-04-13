#!/bin/python3
#Class 7 Python Script
#DJ Choi
#4/12/2022
#Writing python script to encrypt and decrypt a message and file. 

#import libraries
from cryptography.fernet import Fernet
import os
import os.path

#declare functions

#generates key and save it to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#load key
def load_key():
    return open("key.key", "rb").read()

#menu
def menu():
    choice = input("Options:\n[1] Encrypt a file\n[2] Decrypt a file\n[3] Encrypt a message\n[4] Decrypt a message\n[5] Encrypt a folder and all its contents\n[6] Decrypt a folder and all its contents\nEnter a number: ")

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

    elif choice == '5':
        folder = input("Enter foler path: ")
        encrypt_dir(folder)

    elif choice == '6':
        folder = input("Enter folder path: ")
        decrypt_dir(folder)
    else:
        print("Invalid choice. Please try again.")

#checking if key file exist
def key_check():
    if os.path.isfile("./key.key"):
        key = load_key()
    else:
        write_key()
        key = load_key()
    global f
    f = Fernet(key)

#encrypt a message
def encrypt_message(message):
    key_check()
    encrypted = f.encrypt(message)
    print("Ciphertext is "+encrypted.decode('utf-8'))

#decrypt a message
def decrypt_message(message):
    key_check()
    decrypted = f.decrypt(message)
    print("Plaintext is "+str(decrypted.decode('utf-8')))

#encrypt file
def encrypt(filename):
    key_check()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print("File encrypted")

#decrypt file
def decrypt(filename):
    key_check()
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File Decrypted")

#encrypt directory and contents
def encrypt_dir(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_path = (os.path.join(root, name))
            print(file_path)
            encrypt(file_path)
        for name in dirs:
            file_path = (os.path.join(root, name))
            print(file_path)
            encrypt(file_path)

#decrypt directory and contents
def decrypt_dir(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_path = (os.path.join(root, name))
            print(file_path)
            decrypt(file_path)
        for name in dirs:
            file_path = (os.path.join(root, name))
            print(file_path)
            decrypt(file_path)

# Main

menu()

#end



