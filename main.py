import usecase

command = input("Enter Command: ")
if command == 'list':
    listUseCase = usecase.ListUseCase()
    listUseCase.execute()
elif command == '' or command == 'encrypt':
    encryptUseCase = usecase.EncryptPasswordsUseCase()
    encryptUseCase.execute()