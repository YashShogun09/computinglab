from cryptography.fernet import Fernet

# Generate a symmetric key
key = Fernet.generate_key()

# Save the key to a file (or securely transfer it to the receiver)
with open("shared_key.key", "wb") as key_file:
    key_file.write(key)

print(f"[KEY GENERATED] Shared key: {key.decode()}")
