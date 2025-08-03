from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Load public key
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Message to encrypt
message = input("Enter message to encrypt: ").encode()

# Encrypt the message
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save encrypted message to file
with open("encrypted_data.bin", "wb") as f:
    f.write(ciphertext)

print(f"[ENCRYPTION] Message encrypted and saved to encrypted_data.bin")
