from cryptography.fernet import Fernet
import os

# Directory containing the files to "encrypt"
FILES_DIR = "test_files"
# Encryption key file
KEY_FILE = "key.key"

def generate_key():
    """Generate and save a key for encryption."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"Encryption key saved to {KEY_FILE}")

def load_key():
    """Load the encryption key from a file."""
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    """Encrypt a single file and save the encrypted version."""
    with open(file_path, "rb") as file:
        data = file.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    # Save the encrypted file (simulating ransomware)
    with open(f"{file_path}.encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f"File encrypted: {file_path} -> {file_path}.encrypted")

def decrypt_file(file_path, key):
    """Decrypt an encrypted file."""
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Save the decrypted file (restoring original content)
    original_file_path = file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"File decrypted: {file_path} -> {original_file_path}")

def simulate_encryption():
    """Simulate ransomware encryption on all files in FILES_DIR."""
    if not os.path.exists(KEY_FILE):
        generate_key()
    
    key = load_key()
    
    for filename in os.listdir(FILES_DIR):
        file_path = os.path.join(FILES_DIR, filename)
        if os.path.isfile(file_path) and not filename.endswith(".encrypted"):
            encrypt_file(file_path, key)

def simulate_decryption():
    """Simulate ransomware decryption on all encrypted files in FILES_DIR."""
    if not os.path.exists(KEY_FILE):
        print("Encryption key not found.")
        return
    
    key = load_key()
    
    for filename in os.listdir(FILES_DIR):
        file_path = os.path.join(FILES_DIR, filename)
        if os.path.isfile(file_path) and filename.endswith(".encrypted"):
            decrypt_file(file_path, key)

if __name__ == "__main__":
    choice = input("Enter 'E' to simulate encryption or 'D' to simulate decryption: ").strip().upper()
    if choice == 'E':
        simulate_encryption()
    elif choice == 'D':
        simulate_decryption()
    else:
        print("Invalid option. Exiting.")
