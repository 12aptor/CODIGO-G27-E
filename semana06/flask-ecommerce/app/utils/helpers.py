from fernet import Fernet
import os
import base64
from typing import Union

class CryptoHelper:
    def __init__(self):
        self.key = os.getenv('FERNET_SECRET_KEY')
        self.validate_key()
        self.fernet = Fernet(self.key.encode('utf-8'))

    def encrypt(self, value: Union[str, int, float, bool]) -> str:
        bytes_value = str(value).encode('utf-8')
        encrypted_value = self.fernet.encrypt(bytes_value)
        return encrypted_value.decode('utf-8')
    
    def decrypt(self, value: str) -> Union[str, int, float, bool]:
        bytes_value = value.encode('utf-8')
        decrypted_value = self.fernet.decrypt(bytes_value)
        return decrypted_value.decode('utf-8')

    def validate_key(self):
        if not self.key:
            raise ValueError('FERNET_SECRET_KEY is not set')
        
        try:
            bytes_key = base64.urlsafe_b64decode(self.key)

            if len(bytes_key) != 32:
                raise ValueError('Invalid key length')
        except ValueError as e:
            raise ValueError(f'Invalid key: {e}')