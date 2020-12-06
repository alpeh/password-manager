import domain
import gateway
import json

class EncryptPasswordsUseCase:
    def __init__(self):
        self.config = domain.PasswordConfig()
        self.plainTextGateway = gateway.PlainTextFileGateway()
        self.encryptedFileGateway = gateway.EncryptedFileGateway()
    def execute(self):
        passwordFile = self.plainTextGateway.read()
        passwordFile.fileContents = passwordFile.encrypt()
        self.encryptedFileGateway.save(passwordFile)

class ListUseCase:
    def __init__(self):
        self.fileGateway = gateway.EncryptedFileGateway() 
    def execute(self):
        passwordFile = self.fileGateway.read()
        passwordSet = json.loads(passwordFile.decrypt())

        for passwordDetails in passwordSet:
            message = "\nSite: " + passwordDetails['site']
            message += "\nUsername: " + passwordDetails['username']
            message += "\nPassword: " + passwordDetails["password"]
            message += "\nSecurity Questions: "
            message += "\n" 
            print(message)

class DecryptUseCase:
    def __init__(self):
        self.encryptedFileGateway = gateway.EncryptedFileGateway()
        self.plainTextGateway = gateway.PlainTextFileGateway()
    def execute(self):
        passwordFile = self.encryptedFileGateway.read()
        passwordFile.fileContents = passwordFile.decrypt()
        self.plainTextGateway.save(passwordFile)
