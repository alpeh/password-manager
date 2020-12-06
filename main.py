import sys, getopt
import usecase
import domain

argumentList = sys.argv[1:]
shortOptions = 'p:e:d:'
longOptions = ['list', 'encrypt', 'decrypt', 'help', 'password=', 'encryptedFileName=', 'decryptedFileName=']
providedPassword = domain.PasswordConfig.providedPassword
encryptedFileName = domain.PasswordConfig.encryptedPasswordSourceFileName
decryptedFileName = domain.PasswordConfig.passwordSourceFileName

try:
    arguments, currentValue = getopt.getopt(argumentList, shortOptions, longOptions)
    programRequested = arguments[0][0] if len(arguments) > 0 else '--help'
    for currentArgument, currentValue in arguments:
        cleanedValue = currentValue.strip("=")
        if currentArgument in ('--password', '-p'):
            providedPassword = cleanedValue
        elif currentArgument in ('--encryptedFileName', '-e'):
            encryptedFileName = cleanedValue
        elif currentArgument in ('--decryptedFileName', '-d'):
            decryptedFileName = cleanedValue

    domain.PasswordConfig.providedPassword = providedPassword
    domain.PasswordConfig.passwordSourceFileName = decryptedFileName
    domain.PasswordConfig.encryptedPasswordSourceFileName = encryptedFileName

    if programRequested != '--help':
        print("Command: %s" % (programRequested))
        print("Password: %s" % (providedPassword))
        print("Encrpyted Filename: %s" % (encryptedFileName))
        print("Decrypted Filename: %s" % (decryptedFileName))

    if programRequested == '--list':
        usecase = usecase.ListUseCase()
        usecase.execute()
    elif programRequested == '--encrypt':
        usecase = usecase.EncryptPasswordsUseCase()
        usecase.execute()
    elif programRequested == '--decrypt':
        usecase = usecase.DecryptUseCase()
        usecase.execute()
    elif programRequested == '--help':
        print('Commands Supported: ')
        print('Command: --list Description: Lists passwords through command line')
        print('Command: --encrypt Description: Encrptes decrypted file')
        print('Command: --decrypt Description: Decryptes encrypted file')
        print('\nArguments Supported:')
        print('Argument: --password, -p Description: Sets password')
        print('Argument: --encryptedFileName, -e Description: Sets encrypted filename')
        print('Argument: --decryptedFileName, -d Description: Sets decrypted filename')
    
except getopt.error as error:
    print(str(error))
    sys.exit(2)