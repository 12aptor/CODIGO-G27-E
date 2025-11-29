from fernet import Fernet
import os
import base64

class CryptoHelper:
    def __init__(self):
        self.key = os.getenv('FERNET_SECRET_KEY')
        self.validate_key()

    def encrypt(self, value: str) -> str:
        fernet = Fernet(self.key.encode('utf-8'))
        bytes_value = str(value).encode('utf-8')
        encrypted_value = fernet.encrypt(bytes_value)
        return encrypted_value.decode('utf-8')
    
    def decrypt(self, value: str) -> str:        
        fernet = Fernet(self.key.encode('utf-8'))
        bytes_value = fernet.decrypt(value.encode('utf-8'))
        return bytes_value.decode('utf-8')
    
    def validate_key(self):
        if not self.key:
            raise ValueError('FERNET_SECRET_KEY is not set')
        
        try:
            bytes_key = base64.urlsafe_b64decode(self.key)
            if len(bytes_key) != 32:
                raise ValueError('Invalid FERNET_SECRET_KEY length')
        except ValueError as e:
            raise ValueError(f'FERNET_SECRET_KEY is not valid: {e}')