#***********************************************************************************************************
#  
# Aluno: Marco Antonio Monteiro Pedro
# Data 29/12/2024
# Modulo 'Computational Logic Using Python'
# Portifolio
#
#***********************************************************************************************************
#
# A função 'Try/Except' foi implementada para prevenir entradas inválidas do usuário, 
# evitando que o programa seja interrompido devido a erros. Essa abordagem também é 
# aplicada na primeira execução do programa, pois, nesse momento, o arquivo 'txt.' ainda
# não estará disponível e será criado posteriormente. Além disso, foi elaborado um
# bloco 'Try/Except' dentro de um laço 'While True', permitindo que, caso uma entrada
# incorreta seja digitada, o usuário tenha a oportunidade de tentar novamente. O código 
# contém comentários explicativos sobre as linhas e seus funcionamentos para auxiliar na 
# correção e avaliação por parte do professor.
#
#********************************************************************************************************

import sys  # Importa funções e variáveis usadas para manipular o tempo de execução do Python (usado para finalizar o programa).
import time  # Importa funções para trabalhar com tempo, como pausas (time.sleep).
import json  # Importa funções para codificação e decodificação de dados no formato JSON (usado para salvar e carregar dados).


# Dicionário para armazenar eventos
evento = {}
# Variável global para armazenar o tipo de usuário (coordenador ou aluno)
tipo_usuario = ""

# Função para carregar dados dos eventos a partir de um arquivo txt
def carregar_dados():
    global evento
    try:
        with open('eventos.txt', 'r') as file:
            evento = json.load(file)
    except FileNotFoundError:
        evento = {}

# Função para salvar dados dos eventos em um arquivo txt
def salvar_dados():
    with open('eventos.txt', 'w') as file:
        json.dump(evento, file)

# Função para exibir o menu inicial e definir o perfil do usuário
def menu_inicial():
    global tipo_usuario
    while True:
        print('************** Controle de Eventos da UniFECAF **************\n')
        print('Informe seu perfil:\n')
        print('(1) Coordenador\n(2) Aluno\n')
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha == 1:
                tipo_usuario = "coordenador"
                break
            elif escolha == 2:
                tipo_usuario = "aluno"
                break
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.\n")
        time.sleep(2)


# Função para visualizar todos os eventos cadastrados
def visualizar_eventos():
    print("Eventos Atuais:")
    if not evento:
        print("Nenhum evento cadastrado.")
    else:
        for nome, detalhes in evento.items():
            status_vagas = "Lotado" if len(detalhes['Inscritos']) >= detalhes['Quantidade de pessoas permitidas'] else "Vagas Disponíveis"
            print(f"Evento: {nome}")
            print(f"  Descrição: {detalhes['Descrição']}")
            print(f"  Quantidade de pessoas permitidas: {detalhes['Quantidade de pessoas permitidas']}")
            print(f"  Data: {detalhes['Data marcada']}")
            print(f"  Hora: {detalhes['Hora p/ inicio do Evento']}")
            print(f"  Inscritos: {', '.join(detalhes['Inscritos']) if detalhes['Inscritos'] else 'Nenhum inscrito'}")
            print(f"  Status: {status_vagas}")
            print("\n")
    time.sleep(2)

# Função para criar um novo evento
def criar_evento():
    while True:
        try:
            Evento_name = input('Digite o nome do evento: ')
            Descricao = input('Digite a descrição do evento: ')
            Quant_Pess_Perm = int(input('Quantidade de pessoas permitidas nesse evento: '))
            Data_Event = input('Informe a data do evento: ')
            Hora_Event = input('Informe a hora do evento: ')
            
            # Armazenar os detalhes do evento no dicionário
            evento[Evento_name] = {
                'Descrição': Descricao,
                'Quantidade de pessoas permitidas': Quant_Pess_Perm,
                'Data marcada': Data_Event,
                'Hora p/ inicio do Evento': Hora_Event,
                'Inscritos': []
            }
            print(f"Evento {Evento_name} marcado com sucesso.\n")
            salvar_dados()  # Salvar dados no arquivo
            
            # Perguntar se deseja adicionar outro evento
            adicionar_mais = input('Deseja adicionar outro evento? (S/N): ')
            if adicionar_mais.lower() != 's':
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira valores corretos.\n")
        time.sleep(2)


# Função para editar um evento existente
def editar_evento():
    if not evento:
        print("Nenhum evento disponível para edição.")
        return

    Evento_name = input('Digite o nome do evento que deseja editar: ')
    if Evento_name in evento:
        try:
            print(f"Editando evento {Evento_name}")
            Descricao = input('Nova descrição do evento: ')
            Quant_Pess_Perm = int(input('Nova quantidade de pessoas permitidas: '))
            Data_Event = input('Nova data do evento: ')
            Hora_Event = input('Nova hora do evento: ')

            # Atualizar os detalhes do evento no dicionário
            evento[Evento_name] = {
                'Descrição': Descricao,
                'Quantidade de pessoas permitidas': Quant_Pess_Perm,
                'Data marcada': Data_Event,
                'Hora p/ inicio do Evento': Hora_Event,
                'Inscritos': evento[Evento_name]['Inscritos']
            }
            print(f"Evento {Evento_name} atualizado com sucesso.\n")
            salvar_dados()
        except ValueError:
            print("Entrada inválida. Por favor, insira valores corretos.\n")
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

# Função para excluir um evento existente
def excluir_evento():
    if not evento:
        print("Nenhum evento disponível para exclusão.")
        return

    visualizar_eventos()
    Evento_name = input('Digite o nome do evento que deseja excluir: ')
    if Evento_name in evento:
        del evento[Evento_name]
        print(f"Evento {Evento_name} excluído com sucesso.\n")
        salvar_dados()
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

# Função para visualizar os inscritos em um evento específico
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


# Função para inscrever um aluno em um evento
def inscrever_aluno():
    if not evento:
        print("Nenhum evento disponível para inscrição.")
        return

    # Exibir a lista de eventos disponíveis
    print("Eventos Disponíveis:")
    for nome, detalhes in evento.items():
        # Verificar se o número de inscritos é maior ou igual ao número de vagas permitidas
        if len(detalhes['Inscritos']) >= detalhes['Quantidade de pessoas permitidas']:
            status_vagas = "Completo, não tem vagas disponíveis"
        else:
            status_vagas = "Vagas Disponíveis"
        # Exibir o nome do evento e seu status de vagas
        print(f"Evento: {nome}, Status: {status_vagas}")
    print("\n")

    Evento_name = input('Digite o nome do evento que deseja se inscrever: ')
    if Evento_name in evento:
        while len(evento[Evento_name]['Inscritos']) < evento[Evento_name]['Quantidade de pessoas permitidas']:
            Aluno_nome = input('Digite seu nome: ')
            evento[Evento_name]['Inscritos'].append(Aluno_nome)
            print(f"{Aluno_nome} inscrito com sucesso no evento {Evento_name}.\n")
            salvar_dados()

            # Verificar se o evento atingiu o número máximo de inscritos
            if len(evento[Evento_name]['Inscritos']) >= evento[Evento_name]['Quantidade de pessoas permitidas']:
                print(f"O evento {Evento_name} atingiu o número máximo de inscritos.\n")
                break

            # Perguntar se deseja adicionar outra pessoa ao evento
            adicionar_mais = input('Deseja adicionar outra pessoa a este evento? (S/N): ')
            if adicionar_mais.lower() != 's':
                break
    else:
        print(f"O evento {Evento_name} não existe.\n")
    time.sleep(2)

# Função para o menu do coordenador, oferecendo várias opções de gerenciamento de eventos
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
                visualizar_eventos()
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


# Função para o menu principal, permitindo escolher entre a área do aluno e a área da coordenação
def menu_principal():
    while True:
        print('************** Controle de Eventos da UniFECAF **************\n')
        if tipo_usuario == "coordenador":
            print('Escolha a opção:\n')
            print('(1) Área do Aluno (inscrever em eventos) \n(2) Área da Coordenação\n(3) Visualizar Eventos\n(4) Voltar ao Menu Inicial\n(5) Sair\n')
        else:
            print('Escolha a opção:\n')
            print('(1) Área do Aluno (inscrever em eventos) \n(3) Visualizar Eventos\n(4) Voltar ao Menu Inicial\n(5) Sair\n')
        try:
            Escolha_Usuario = int(input("Digite a opção desejada: "))
            if Escolha_Usuario == 1:
                inscrever_aluno()
            elif Escolha_Usuario == 2 and tipo_usuario == "coordenador":
                menu_cordenador()
            elif Escolha_Usuario == 3:
                visualizar_eventos()
                if not evento:
                    time.sleep(2)
            elif Escolha_Usuario == 4:
                return  # Voltar ao menu inicial
            elif Escolha_Usuario == 5:
                print("Saindo do programa...")
                time.sleep(1)
                sys.exit()  # Finaliza o programa
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.\n")
        time.sleep(2)


# Função para iniciar o programa
def iniciar_programa():
    carregar_dados()  # Carregar dados ao iniciar o programa
    while True:
        menu_inicial()
        menu_principal()
        

# Iniciar o programa
iniciar_programa()
