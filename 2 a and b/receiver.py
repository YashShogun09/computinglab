from cryptography.fernet import Fernet

# Load the shared key
with open("shared_key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Simulate receiving (read from file or network)
with open("encrypted_message.txt", "rb") as f:
    encrypted_message = f.read()

# Decrypt the message
decrypted = fernet.decrypt(encrypted_message)

print(f"[RECEIVER] Decrypted message: {decrypted.decode()}")
