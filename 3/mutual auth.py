import secrets
import hashlib

# Shared secret known only to both parties
SHARED_SECRET = "super_secret_key"

def generate_challenge():
    return secrets.token_hex(8)

def compute_response(challenge):
    return hashlib.sha256((challenge + SHARED_SECRET).encode()).hexdigest()

# --- Alice side ---
alice_challenge = generate_challenge()
print("Alice → Bob challenge:", alice_challenge)

# --- Bob side verifies Alice and sends his own challenge ---
bob_response = compute_response(alice_challenge)
bob_challenge = generate_challenge()
print("Bob → Alice response:", bob_response)
print("Bob → Alice challenge:", bob_challenge)

# --- Alice verifies Bob and sends response back ---
alice_response = compute_response(bob_challenge)
print("Alice → Bob response:", alice_response)

# --- Mutual verification ---
if bob_response == compute_response(alice_challenge):
    print("✅ Bob authenticated Alice")
if alice_response == compute_response(bob_challenge):
    print("✅ Alice authenticated Bob")
