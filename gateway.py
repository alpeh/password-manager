import domain;

class EncryptedFileGateway:
    def __init__(self):
        self.config = domain.PasswordConfig()
    def save(self, passwordFile):
        f = open(self.config.encryptedPasswordSourceFileName, 'w')
        f.write(passwordFile.fileContents)
        f.close()
    def read(self):
        fileContents = ""
        with open(self.config.encryptedPasswordSourceFileName, 'r') as fileResource:
            fileContents += fileResource.read()
        passwordFile = domain.PasswordFile()
        passwordFile.fileContents = fileContents 
        return passwordFile

class PlainTextFileGateway:
    def __init__(self):
        self.config = domain.PasswordConfig()
    def read(self):
        fileContents = ""
        with open(self.config.passwordSourceFileName, 'r') as fileResource:
            fileContents += fileResource.read()
        passwordFile = domain.PasswordFile()
        passwordFile.fileContents = fileContents
        return passwordFile
    def save(self, passwordFile):
        f = open(self.config.passwordSourceFileName, 'w')
        f.write(passwordFile.fileContents)
        f.close()
