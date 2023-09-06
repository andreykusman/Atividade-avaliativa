# Dicionário global para armazenar os usuários
banco_usuarios = []

# Função para cadastrar um usuário com campos flexíveis
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    # Preenche os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    
    # Pede e preenche campos extras até que 'sair' seja digitado
    while True:
        campo_extra = input("Digite um campo extra (ou 'sair' para encerrar): ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"Digite o valor para o campo '{campo_extra}': ")
        usuario[campo_extra] = valor_extra
    
    # Adiciona o usuário ao banco de usuários
    banco_usuarios.append(usuario)
    return usuario

# Função para imprimir usuários com várias opções
def imprimir_usuarios(*args, **kwargs):
    opcao = input("Digite a opção (1 - imprimir todos, 2 - filtrar por nomes, 3 - filtrar por campos, 4 - filtrar por nomes e campos): ")
    
    if opcao == '1':
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == '2':
        # Filtra e imprime usuários por nomes
        for nome in args:
            for usuario in banco_usuarios:
                if usuario.get('nome') == nome:
                    print(usuario)
    elif opcao == '3':
        # Filtra e imprime usuários por campo específico
        campo_busca = input("Digite o campo de busca: ")
        valor_busca = input(f"Digite o valor para o campo '{campo_busca}': ")
        for usuario in banco_usuarios:
            if usuario.get(campo_busca) == valor_busca:
                print(usuario)
    elif opcao == '4':
        # Filtra e imprime usuários por nomes e campos específicos
        nomes = input("Digite os nomes (separados por vírgula): ").split(',')
        campos = input("Digite os campos (separados por vírgula): ").split(',')
        
        for usuario in banco_usuarios:
            if usuario.get('nome') in nomes:
                dados_correspondentes = True
                for campo in campos:
                    valor_campo = input(f"Digite o valor para o campo '{campo}' de '{usuario['nome']}': ")
                    if usuario.get(campo) != valor_campo:
                        dados_correspondentes = False
                        break
                
                if dados_correspondentes:
                    print(usuario)

# Função principal do programa
def main():
    campos_obrigatorios = input("Digite os campos obrigatórios (separados por vírgula): ").split(',')
    
        # Loop principal que mantém o programa em execução
    while True:
        # Exibe o menu de opções
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("3 - Sair")
        
        # Solicita ao usuário que escolha uma opção
        escolha = input("Escolha uma opção: ")
        
        # Verifica a escolha do usuário e executa a ação correspondente
        if escolha == '1':
            # Se a escolha for '1', cadastra um novo usuário
            usuario_cadastrado = cadastrar_usuario(campos_obrigatorios)
            print(f"Usuário cadastrado: {usuario_cadastrado}")
        elif escolha == '2':
            # Se a escolha for '2', imprime os usuários
            imprimir_usuarios()
        elif escolha == '3':
            # Se a escolha for '3', sai do programa encerrando o loop
            break
        else:
            # Se a escolha não for válida, exibe uma mensagem de erro
            print("tentativa inválida. Tente novamente.")
if __name__ == "__main__":
    main()

