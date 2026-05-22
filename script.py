import random
import string
import hashlib

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("=== Hackerocked Python Tool ===")
    new_pass = generate_password()
    print(f"[+] Generated Password: {new_pass}")

    hash_object = hashlib.sha256(new_pass.encode())
    hex_dig = hash_object.hexdigest()
    print(f"[+] SHA-256 Hash: {hex_dig}")
