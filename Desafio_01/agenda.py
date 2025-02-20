# Executar "app.py" para rodar o programa

def adicionar_contato(contatos, nome, telefone, email):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"Contato {nome} foi adicionado a sua agenda.")
  return

def adicionar_favorito(contatos, indice_contato):
  indice_contato_ajustato = int(indice_contato) -1
  contato = contatos[indice_contato_ajustato]
  contato["favorito"] = contato["nome"]
  print(f"Contato {indice_contato} adicionado aos favoritos")
  return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]

        print(f"{indice}. {status} {nome_contato} | Telefone: {telefone_contato} | E-mail: {email_contato}")
    return

def ver_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    favoritos_encontrados = False

    for indice, contato in enumerate(contatos, start=1):
        if "favorito" in contato and contato["favorito"]:  # Verifica se "favorito" existe e é True
            status = "★"
            nome_contato = contato["nome"] if "nome" in contato else "Sem Nome"
            telefone_contato = contato["telefone"] if "telefone" in contato else "Sem Telefone"
            email_contato = contato["email"] if "email" in contato else "Sem Email"

            print(f"{indice}. {status} {nome_contato} | Telefone: {telefone_contato} | E-mail: {email_contato}")
            favoritos_encontrados = True

    if not favoritos_encontrados:
        print("Nenhum contato favorito encontrado.")
    return

def editar_contato(contatos, indice_contato, campo, novo_valor):
    try:
        # Ajusta o índice para começar do 0
        indice_contato_ajustado = int(indice_contato) - 1
        contato = contatos[indice_contato_ajustado]

        # Verifica se o campo é válido
        if campo in contato:
            contato[campo] = novo_valor
            print(f"\nContato {indice_contato} atualizado: Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']}")
        else:
            print("Erro: Campo inválido.")

    except (IndexError, ValueError):
        print("Erro: Índice inválido. Verifique se o número está correto.")

def deletar_contato(contatos, indice_contato):
    contato_removido = contatos.pop(indice_contato)  # Remove o contato pelo índice
    print(f"Contato '{contato_removido['nome']}' removido com sucesso.")

def remover_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1

    favorito_removido = contatos[indice_contato_ajustado]  # Obtém o contato

    # Remove o status de favorito
    favorito_removido["favorito"] = False
    print(f"Contato '{favorito_removido['nome']}' removido dos favoritos.")

contatos = []
