import base64, hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordConfig:
    providedPassword = ""
    passwordSourceFileName = "..\source\passwords.json"
    encryptedPasswordSourceFileName = "..\source\enc-passwords.data"

class PasswordManager:
    def __init__(self):
        self.passwordProvided = PasswordConfig.providedPassword
        self.salt = "_salt_"
    def getKey(self):
        encodedPassword = self.passwordProvided.encode()
        salt = b'_salt_'
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(encodedPassword))
    def encrypt(self, token):
        key = self.getKey()
        f = Fernet(key)
        return f.encrypt(token.encode())
    def decrypt(self, token):
        key = self.getKey()
        f = Fernet(key)
        return f.decrypt(token)

class PasswordFile:
    def __init__(self):
        self.config = PasswordConfig()
        self.passwordManager = PasswordManager()
        self.fileContents = ""
    def decrypt(self):
        fileContents = self.passwordManager.decrypt(bytes(self.fileContents, 'utf-8'))
        return fileContents.decode()
    def encrypt(self):
        encryptedBytes = self.passwordManager.encrypt(self.fileContents)
        return encryptedBytes.decode()