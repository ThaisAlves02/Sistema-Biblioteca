print("=== Bem vindo(a) a biblioteca online ===")

livros = []
while True:
    print("""
        ------- MENU -------
    1. Cadastrar livros
    2. Vizualizar livros
    3. Ver detalhes
        
    0. Sair
    """) # passo 3


    print("Digite a opção desejada: ")
    op = input("---> ")

    if op == "1":
        while True:
            print("Cadastro de livros")
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            genero = input("Digite o gênero do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")
            isbn = input("Digite o ISBN do livro: ")

            livro = {
                "Titulo": titulo,
                "Autor": autor,
                "Gênero": genero,
                "Ano de publicação": ano_publicacao,
                "ISBN": isbn
            }

            livros.append(livro)
            print("Livro cadastrado com sucesso!")

