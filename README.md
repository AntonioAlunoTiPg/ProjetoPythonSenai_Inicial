# Projeto Agenda de Contatos

## Objetivo da Agenda

Este programa Python foi desenvolvido para funcionar como uma agenda de contatos **simples e funcional**. Seu principal objetivo é permitir que o usuário gerencie informações de contato de forma eficiente, armazenando e recuperando dados diretamente em um **banco de dados SQLite local**.

A aplicação oferece as funcionalidades essenciais (CRUD - Create, Read, Update, Delete), adaptadas para o contexto de uma agenda:

* **Adicionar Contatos:** Permite cadastrar novos contatos com **nome**, **telefone**, **CPF** e **endereço**.
* **Listar Contatos:** Exibe todos os contatos salvos na agenda, mostrando todas as suas informações.
* **Buscar Contatos:** Possibilita encontrar contatos específicos através da busca por parte do nome.
* **Remover Contatos:** Oferece a capacidade de excluir contatos da agenda usando seu ID exclusivo.

O programa foi projetado para ser intuitivo, com um menu interativo de linha de comando que guia o usuário pelas opções disponíveis.

---

## Como Executar o Programa

Para rodar este programa em seu ambiente local, siga os passos abaixo:

1.  **Pré-requisitos:**
    * **Python:** Certifique-se de ter o Python 3.x instalado em seu sistema operacional. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
    * **VS Code (Opcional, mas Recomendado):** Para uma melhor experiência de desenvolvimento e execução, utilize o Visual Studio Code com a extensão Python instalada.

2.  **Preparação:**
    * Crie uma pasta vazia em seu computador para o projeto (ex: `minha_agenda_python`).
    * Salve o código Python fornecido em um arquivo com a extensão `.py` dentro desta pasta (ex: `agenda_app.py`).

3.  **Execução:**
    * **No VS Code:**
        1.  Abra a pasta do projeto (`minha_agenda_python`) no VS Code (`File > Open Folder...`).
        2.  Abra o arquivo `agenda_app.py`.
        3.  Clique no botão **"Run Python File" (triângulo verde)** localizado no canto superior direito do editor. O programa será executado no terminal integrado do VS Code.
    * **Via Terminal/Prompt de Comando:**
        1.  Abra o terminal ou prompt de comando.
        2.  Navegue até a pasta onde você salvou o arquivo `agenda_app.py` usando o comando `cd` (ex: `cd minha_agenda_python`).
        3.  Execute o script com o comando: `python agenda_app.py` (ou `python3 agenda_app.py`, dependendo da sua configuração).

4.  **Primeira Execução e Banco de Dados:**
    * Na primeira vez que você rodar o programa, ele criará automaticamente um arquivo de banco de dados chamado `agenda.db` na mesma pasta do script.
    * **Importante:** Se você já rodou o programa antes e a estrutura da tabela `contatos` foi alterada (como a adição dos campos CPF e Endereço), você precisará **excluir o arquivo `agenda.db` existente** antes de executar o programa novamente. Isso garantirá que a tabela seja recriada com a estrutura mais recente.

Após a execução, o programa apresentará um menu interativo no terminal, permitindo que você realize as operações da agenda.

---

## Créditos do Aluno

**Desenvolvido por:** [Antonio Victor Monteiro de Souza]
**Disciplina/Curso:** [Programação Senai]
**Data:** [Concluido 03/07/2025/Ultimo commit as 20:19, julho de 2025]