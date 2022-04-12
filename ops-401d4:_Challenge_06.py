#!/bin/python3
#Class 6 Python Script
#DJ Choi
#4/11/2022
#Writing python



# Import Libraries
from cryptography.fernet import Fernet

# Declare Functions

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

def encrypt(filename, key):
    #Given a filename (str) and key (bytes), it encrypts the file and write it
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt2(filename, key):
    #Given a filename (str) and key (bytes), it decrypts the file and write it
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
# Main

ip  = input("enter")

# Generate and write a new key
write_key()

# load the previously generated key
key = load_key()
#print("Key is "+str(key.decode('utf-8')))

message = ip.encode()
print("Plaintext is "+str(message.decode('utf-8')))

# Initialize the Fernet class
f = Fernet(key)

# Encrypt the message
encrypted = f.encrypt(message)

# Print how it looks
print("Ciphertext is "+encrypted.decode('utf-8'))

print()
# Decrypt the message
#decrypted = f.decrypt(ip)
#print(decrypted)

#file name
#file = "data.csv"
#encrypt
#encrypt(file, key)

#decrypt
#decrypt(file, key)
