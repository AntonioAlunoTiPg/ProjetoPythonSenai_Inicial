import sqlite3


def criar_conexao():
    """
    Cria e retorna uma conexão com o banco de dados SQLite 'agenda.db'.

    Se o banco de dados não existir, ele será criado.

    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados.
    """
    return sqlite3.connect("agenda.db")


 
## Estrutura do Banco de Dados
 

def criar_tabela():
    """
    Cria a tabela 'contatos' no banco de dados, se ela ainda não existir.

    A tabela inclui os campos:
    - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    - nome (TEXT NOT NULL)
    - telefone (TEXT NOT NULL)
    - cpf (TEXT, pode ser NULL)
    - endereco (TEXT, pode ser NULL)
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cpf TEXT,
            endereco TEXT
        )
    """)
    conexao.commit()
    conexao.close()


 
## Funções de Manipulação de Contatos
 

def adicionar_contato(nome, telefone, cpf, endereco):
    """
    Adiciona um novo contato à tabela 'contatos'.

    Args:
        nome (str): O nome do contato.
        telefone (str): O número de telefone do contato.
        cpf (str): O CPF do contato (pode ser uma string vazia para NULL).
        endereco (str): O endereço do contato (pode ser uma string vazia para NULL).
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO contatos (nome, telefone, cpf, endereco) VALUES (?, ?, ?, ?)",
        (nome, telefone, cpf, endereco)
    )
    conexao.commit()
    conexao.close()
    print("Contato adicionado com sucesso!")


def listar_contatos():
    """
    Lista todos os contatos presentes na tabela 'contatos'.

    Exibe ID, Nome, Telefone, CPF e Endereço de cada contato.
    Se os campos de CPF ou Endereço estiverem vazios no banco,
    'N/A' será exibido no lugar.
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    if contatos:
        print("\n--- Lista de Contatos ---")
        for contato in contatos:
            # Acessa os campos pelos índices da tupla resultante da query.
            # Usa 'or "N/A"' para mostrar "N/A" se o valor no banco for NULL (None em Python).
            print(
                f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, "
                f"CPF: {contato[3] or 'N/A'}, Endereço: {contato[4] or 'N/A'}"
            )
        print("-------------------------")
    else:
        print("Nenhum contato encontrado.")
    conexao.close()


def buscar_contato_por_nome(nome):
    """
    Busca contatos na tabela 'contatos' por uma parte do nome e exibe suas informações.

    A busca é case-insensitive para SQLite.
    Exibe 'N/A' se os campos de CPF ou Endereço estiverem vazios.

    Args:
        nome (str): A parte do nome a ser buscada.
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    # Usa LIKE e % para permitir busca por parte do nome (case-insensitive para SQLite).
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    if resultados:
        print(f"\n--- Resultados da Busca por '{nome}' ---")
        for resultado in resultados:
            print(
                f"ID: {resultado[0]}, Nome: {resultado[1]}, Telefone: {resultado[2]}, "
                f"CPF: {resultado[3] or 'N/A'}, Endereço: {resultado[4] or 'N/A'}"
            )
        print("---------------------------------------")
    else:
        print(f"Nenhum contato encontrado com o nome '{nome}'.")
    conexao.close()


def remover_contato_por_id(contato_id):
    """
    Remove um contato da tabela 'contatos' pelo seu ID.

    Args:
        contato_id (int): O ID do contato a ser removido.
    """
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (contato_id,))
    conexao.commit()
    conexao.close()
    print("Contato removido com sucesso!")


 
## Menu Principal
 

def menu():
    """
    Exibe o menu principal da agenda e gerencia as interações do usuário.

    Garante que a tabela de contatos seja criada (ou atualizada se o DB for novo)
    antes de exibir o menu.
    """
    criar_tabela()

    while True:
        print("\n   --- Menu da Agenda ---")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato por nome")
        print("4 - Remover contato por ID")
        print("5 - Sair")
        print("------------------------")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF (opcional, ex: 123.456.789-00): ")
            endereco = input("Endereço (opcional, ex: Rua A, 123, Bairro X): ")
            adicionar_contato(nome, telefone, cpf, endereco)
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            nome = input("Digite o nome (ou parte dele) para buscar: ")
            buscar_contato_por_nome(nome)
        elif opcao == "4":
            try:
                contato_id = int(input("Digite o ID do contato a remover: "))
                remover_contato_por_id(contato_id)
            except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        elif opcao == "5":
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")


# Este bloco garante que o menu só será executado quando o script for rodado diretamente
if __name__ == "__main__":
    menu()