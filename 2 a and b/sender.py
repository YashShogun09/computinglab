from cryptography.fernet import Fernet

# Load the shared key
with open("shared_key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Get message to send
message = input("Enter message to encrypt and send: ").encode()

# Encrypt the message
encrypted = fernet.encrypt(message)

print(f"[SENDER] Encrypted message: {encrypted.decode()}")

# Simulate sending (write to file or send over network)
with open("encrypted_message.txt", "wb") as f:
    f.write(encrypted)
