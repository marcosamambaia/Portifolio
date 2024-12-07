import time

# Dicionário para armazenar os eventos
evento = {}

def visualizar_eventos():
    print("Eventos Atuais:")
    if not evento:
        print("Nenhum evento cadastrado.")
    else:
        for nome, detalhes in evento.items():
            print(f"Evento: {nome}")
            print(f"  Quantidade de pessoas permitidas: {detalhes['Quantidade de pessoas permitidas']}")
            print(f"  Data: {detalhes['Data marcada']}")
            print(f"  Hora: {detalhes['Hora p/ inicio do Evento']}")
            print(f"  Inscritos: {', '.join(detalhes['Inscritos']) if detalhes['Inscritos'] else 'Nenhum inscrito'}")
            print("\n")
    time.sleep(2)
    while True:
        voltar = input('Deseja voltar ao menu principal? (S/N): ')
        if voltar.lower() == 's':
            break
        elif voltar.lower() == 'n':
            pass
        else:
            print("Opção inválida. Tente novamente.\n")
    time.sleep(2)

def criar_evento():
    while True:
        try:
            Evento_name = input('Digite o nome do evento: ')
            Quant_Pess_Perm = int(input('Quantidade de pessoas permitidas nesse evento: '))
            Data_Event = input('Informe a data do evento: ')
            Hora_Event = input('Informe a hora do evento: ')
            evento[Evento_name] = {'Quantidade de pessoas permitidas': Quant_Pess_Perm, 'Data marcada': Data_Event, 'Hora p/ inicio do Evento': Hora_Event, 'Inscritos': []}
            print(f"Evento {Evento_name} marcado com sucesso.\n")
            adicionar_mais = input('Deseja adicionar outro evento? (S/N): ')
            if adicionar_mais.lower() != 's':
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira valores corretos.\n")
        time.sleep(2)

def editar_evento():
    if not evento:
        print("Nenhum evento disponível para edição.")
        return

    visualizar_eventos()
    Evento_name = input('Digite o nome do evento que deseja editar: ')
    if Evento_name in evento:
        try:
            print(f"Editando evento {Evento_name}")
            Quant_Pess_Perm = int(input('Nova quantidade de pessoas permitidas: '))
            Data_Event = input('Nova data do evento: ')
            Hora_Event = input('Nova hora do evento: ')
            evento[Evento_name] = {'Quantidade de pessoas permitidas': Quant_Pess_Perm, 'Data marcada': Data_Event, 'Hora p/ inicio do Evento': Hora_Event, 'Inscritos': evento[Evento_name]['Inscritos']}
            print(f"Evento {Evento_name} atualizado com sucesso.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira valores corretos.\n")
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

def excluir_evento():
    if not evento:
        print("Nenhum evento disponível para exclusão.")
        return

    visualizar_eventos()
    Evento_name = input('Digite o nome do evento que deseja excluir: ')
    if Evento_name in evento:
        del evento[Evento_name]
        print(f"Evento {Evento_name} excluído com sucesso.\n")
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

def visualizar_inscritos():
    if not evento:
        print("Nenhum evento disponível.")
        return

    print("Eventos Disponíveis:")
    for nome in evento.keys():
        print(f"- {nome}")
    print("\n")

    Evento_name = input('Digite o nome do evento para visualizar os inscritos: ')
    if Evento_name in evento:
        inscritos = evento[Evento_name]['Inscritos']
        if inscritos:
            print(f"Inscritos no evento {Evento_name}:")
            for aluno in inscritos:
                print(aluno)
            while True:
                voltar = input('Deseja voltar ao menu principal? (S/N): ')
                if voltar.lower() == 's':
                    break
                elif voltar.lower() == 'n':
                    pass
                else:
                    print("Opção inválida. Tente novamente.\n")
        else:
            print(f"Ninguém está cadastrado no evento {Evento_name}.")
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

def inscrever_aluno():
    if not evento:
        print("Nenhum evento disponível para inscrição.")
        return

    print("Eventos Disponíveis:")
    for nome, detalhes in evento.items():
        status_vagas = "Completo" if len(detalhes['Inscritos']) >= detalhes['Quantidade de pessoas permitidas'] else "Vagas Disponíveis"
        print(f"Evento: {nome}, Status: {status_vagas}")
    print("\n")

    Evento_name = input('Digite o nome do evento que deseja se inscrever: ')
    if Evento_name in evento:
        while len(evento[Evento_name]['Inscritos']) < evento[Evento_name]['Quantidade de pessoas permitidas']:
            Aluno_nome = input('Digite seu nome: ')
            evento[Evento_name]['Inscritos'].append(Aluno_nome)
            print(f"{Aluno_nome} inscrito com sucesso no evento {Evento_name}.\n")
            if len(evento[Evento_name]['Inscritos']) >= evento[Evento_name]['Quantidade de pessoas permitidas']:
                print(f"O evento {Evento_name} atingiu o número máximo de inscritos.\n")
                break
            adicionar_mais = input('Deseja adicionar outra pessoa a este evento? (S/N): ')
            if adicionar_mais.lower() != 's':
                break
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

def menu_cordenador():
    while True:
        print('Escolha a opção: \n\n (1) Visualizar Eventos\n (2) Criar Eventos\n (3) Editar Eventos\n (4) Excluir Eventos\n (5) Visualizar Inscritos\n (6) Voltar ao menu principal\n')
        try:
            Opcao_Cordenador = int(input("Digite a opção desejada: "))
            if Opcao_Cordenador == 1:
                visualizar_eventos()
            elif Opcao_Cordenador == 2:
                criar_evento()
            elif Opcao_Cordenador == 3:
                editar_evento()
            elif Opcao_Cordenador == 4:
                excluir_evento()
            elif Opcao_Cordenador == 5:
                visualizar_inscritos()
            elif Opcao_Cordenador == 6:
                break
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.\n")
        time.sleep(2)

def menu_principal():
    while True:
        print('************** Controle de Eventos da UniFECAF **************\n')
        print('Digite 1 para área do aluno ou 2 para área da coordenação:\n')
        print('(1) Área do Aluno (inscrever em eventos) \n(2) Área da Coordenação\n(3) Visualizar Eventos\n(4) Sair\n')
        try:
            Escolha_Usuario = int(input("Digite a opção desejada: "))
            if Escolha_Usuario == 1:
                inscrever_aluno()
            elif Escolha_Usuario == 2:
                menu_cordenador()
            elif Escolha_Usuario == 3:
                visualizar_eventos()
                if not evento:
                    time.sleep(2)
            elif Escolha_Usuario == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.\n")
        time.sleep(2)

# Iniciar o menu principal
menu_principal()
