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



menu_options = {
    1: "op1",
    2: "opt2",
    3: "opt3",
    4: "opt4",
}

def print_menu():
    for key in menu_options.key():
        print (key, "--", menu_options[key])
while(True):
    print_menu()
    option = int(input("Enter your choice:"))

input4 = "Hello"
# Generate and write a new key
write_key()

# load the previously generated key
key = load_key()
#print("Key is "+str(key.decode('utf-8')))

message = input4.encode()
#print("Plaintext is "+str(message.decode('utf-8')))

# Initialize the Fernet class
f = Fernet(key)

# Encrypt the message
encrypted = f.encrypt(message)
print(encrypted)
# Print how it looks
print("Ciphertext is "+encrypted.decode('utf-8'))

print()
# Decrypt the message
decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)

#file name
#file = "data.csv"
#encrypt
#encrypt(file, key)

#decrypt
#decrypt(file, key)
