# Executar "app.py" para rodar o programa

from agenda import (
  adicionar_contato,
  adicionar_favorito,
  ver_contatos,
  ver_favoritos,
  deletar_contato,
  remover_favorito,
  editar_contato,
  contatos)

def rodar_menu():
  while True:
    print("\nMenu de gerendiador de lista de contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Ver contatos favoritos")
    print("4. Editar contato")
    print("5. Adicionar contato aos favoritos")
    print("6. Remover contato dos favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1": # Adicionar contato
      nome = input("Digite o nome do contato que deseja adicionar: ")
      telefone= input("Digite o número de telefone do contato: ")
      email = input("Digite o e-mail do contato: ")
      adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2": # Ver contatos
      ver_contatos(contatos)

    elif escolha == "3": # Ver favoritos
      ver_favoritos(contatos)

    elif escolha == "4":  # Editar contato
          ver_contatos(contatos)  # Exibe a lista de contatos antes da edição

          # Solicita o número do contato e verifica se é válido
          try:
              indice_contato = int(input("Digite o número do contato que deseja editar: "))
              
              # Verifica se o índice é válido
              if indice_contato < 1 or indice_contato > len(contatos):
                  print("Contato inválido. Por favor, escolha um número de contato válido.")
                  continue  # Volta para a próxima iteração do loop e pede o número novamente
          except ValueError:
              print("Por favor, digite um número válido.")
              continue  # Volta para a próxima iteração do loop

          print("\nO que deseja editar?")
          print("1 - Nome")
          print("2 - Telefone")
          print("3 - Email")
          opcao = input("Digite o número da opção desejada: ")

          # Verifica se a opção é válida
          if opcao not in ["1", "2", "3"]:
              print("Opção inválida. Escolha 1, 2 ou 3.")
              continue  # Volta para a próxima iteração do loop e pede a opção novamente

          # Se a opção for válida, prossegue com a edição
          indice_contato_ajustado = indice_contato - 1
          contato = contatos[indice_contato_ajustado]

          if opcao == "1":  # Editar nome
              novo_nome = input(f"Digite o novo nome do contato (atual: {contato['nome']}): ")
              if novo_nome.strip():  # Se o usuário digitar algo
                  editar_contato(contatos, indice_contato, "nome", novo_nome)
              else:
                  print("Nome não alterado.")

          elif opcao == "2":  # Editar telefone
              novo_telefone = input(f"Digite o novo número de telefone (atual: {contato['telefone']}): ")
              if novo_telefone.strip():
                  editar_contato(contatos, indice_contato, "telefone", novo_telefone)
              else:
                  print("Telefone não alterado.")

          elif opcao == "3":  # Editar email
              novo_email = input(f"Digite o novo e-mail (atual: {contato['email']}): ")
              if novo_email.strip():
                  editar_contato(contatos, indice_contato, "email", novo_email)
              else:
                  print("E-mail não alterado.")

    elif escolha == "5": # Adicionar favorito
      ver_contatos(contatos)

      if not contatos:  # Verifica se há contatos na lista
          print("A lista de contatos está vazia.")
          continue 
      try:
          indice_contato = int(input("Digite o número do contato que deseja adicionar aos favoritos: "))

           # Verifica se o índice é válido
          if indice_contato < 1 or indice_contato > len(contatos):
              print("Contato inválido. Escolha um número válido.")
              continue
      except ValueError:
          print("Entrada inválida. Digite um número válido.")
          continue
      
      adicionar_favorito(contatos, indice_contato)

    elif escolha == "6":  # Remover dos favoritos
      ver_favoritos(contatos)  # Mostra a lista de contatos

      if not contatos:  # Verifica se há contatos na lista
          print("A lista de contatos está vazia.")
          continue  

      try:
          indice_contato = int(input("Digite o número do contato que deseja remover dos favoritos: "))

          # Verifica se o índice é válido
          if indice_contato < 1 or indice_contato > len(contatos):
              print("Contato inválido. Escolha um número válido.")
              continue
          
          contato = contatos[indice_contato - 1] 

          # Verifica se o contato está nos favoritos
          if not contato["favorito"]:
              print("Este contato não está na lista de favoritos.")
              continue

      except ValueError:
          print("Entrada inválida. Digite um número válido.")
          continue

      remover_favorito(contatos, indice_contato)  # Chama a função para remover dos favoritos

    elif escolha == "7":  # Deletar contato
      ver_contatos(contatos)

      if not contatos:  # Verifica se há contatos na lista
          print("A lista de contatos está vazia.")
          continue  

      try:
          indice_contato = int(input("Digite o número do contato que deseja deletar: "))

          # Verifica se o índice é válido
          if indice_contato < 1 or indice_contato > len(contatos):
              print("Contato inválido. Escolha um número válido.")
              continue

          deletar_contato(contatos, indice_contato - 1)  # Ajusta o índice para a função

      except ValueError:
          print("Entrada inválida. Digite um número válido.")

    elif escolha == "8": # Sair
      print("P R O G R A M A  F I N A L I Z A D O ")
      break
