from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message
message = b"This is a secret message."
encrypted_message = cipher.encrypt(message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")