from fernet import Fernet
import os
import base64
from typing import Union
import cloudinary
import cloudinary.uploader
import cloudinary.utils

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

class CloudinaryHelper:
    def __init__(self):
        cloudinary.config(
            cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
            api_key=os.getenv('CLOUDINARY_API_KEY'),
            api_secret=os.getenv('CLOUDINARY_API_SECRET'),
            secure=True
        )

    def upload_image(self, file, folder='products'):
        try:
            response = cloudinary.uploader.upload(
                file,
                folder=folder
            )
            secure_url = response.get('secure_url')
            public_id = response.get('public_id')
            return secure_url, public_id
        except Exception as e:
            return None
        
    def delete_image(self, public_id):
        try:
            cloudinary.uploader.destroy(public_id)
            return True
        except Exception as e:
            return False

    def get_secure_url(self, public_id):
        try:
            secure_url = cloudinary.utils.cloudinary_url(public_id, secure=True)
            return secure_url[0]
        except Exception as e:
            return None