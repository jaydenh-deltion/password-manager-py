from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
import base64
import os 
import hashlib

class PasswordManager:
    @staticmethod
    def generate_key_sha256(master_password: str, salt: bytes = None) -> tuple:
        """ Handels encryption and decription using sha256
         
        Generate a encription key from master password using sha 256 hashing.
        returns: Key and salt used for hashing
           """
        if salt is None: # salt generate a 16 byte 
            salt = os.urandom(16) # generate a new salt if not provided

        kdf = PBKDF2( # use PBKDF2 key derivation function
            algorithm=hashes.SHA256(), # use SHA-256 hashing algorithm
            length=32, # length of the derived key
            salt=salt, # salt for key derivation
            iterations=100000, # number of iterations for key stretching 
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode())) # derive the key and encode it in urlsafe base64
        return key, salt
    
    @staticmethod
    def encrypt_password(password: str, master_password: str, salt: bytes = None) -> tuple:
        """        Encrypt a password using master password with SHA-256
        Returns: (encrypted_password, salt)"""

        key, salt = PasswordManager.generate_key_sha256(master_password, salt)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(password.encode())
        return encrypted.decode(), salt
    
    @staticmethod
    def decrypt_password( encrypted_password: str, master_password: str, salt: bytes) -> str:
        """ 
        Decrypt a password using master password and salt
        Returns: decrypted password
        """
        try: 
            key, _ = PasswordManager.generate_key_sha256(master_password, salt)
            Fernet = Fernet(key)
            decrypted = Fernet.decrypt(encrypted_password.encode())
            return decrypted.decode()
        except Exception as e:
            raise ValueError ("Decryption failed. Check your master password.") 
        
        @staticmethod
        def hash_password_sha256(password: str) -> str:
            """
        Hash a password using SHA-256 (for comparison purposes)
        Note: For user login passwords, use werkzeug's generate_password_hash instead
        """
        return hashlib.sha256(password.encode()).hexdigest()
    