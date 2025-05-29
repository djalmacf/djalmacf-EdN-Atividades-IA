def verifica_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        
        # Verifica se o usuário quer sair
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        # Verifica o comprimento da senha
        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue
        
        # Verifica se a senha contém um número
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue
        
        # Se chegou até aqui, a senha é válida
        print("Senha forte e válida!")
        break

verifica_senha()
