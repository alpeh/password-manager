import sys, getopt
import usecase

argumentList = sys.argv[1:]
shortOptions = ''
longOptions = ['list', 'encrypt', 'decrypt']

try:
    arguments, values = getopt.getopt(argumentList, shortOptions, longOptions)
    programRequested = arguments[0][0] if len(arguments) > 0 else ''
    
    if programRequested == '--list':
        usecase = usecase.ListUseCase()
        usecase.execute()
    elif programRequested == '--encrypt':
        usecase = usecase.EncryptPasswordsUseCase()
        usecase.execute()
    elif programRequested == '--decrypt':
        usecase = usecase.DecryptUseCase()
        usecase.execute()
    
except getopt.error as error:
    print(str(error))
    sys.exit(2)