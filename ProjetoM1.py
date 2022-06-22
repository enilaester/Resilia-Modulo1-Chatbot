""" Início da estrutura do código
    Nosso projeto aborda um Chatbot automatizado de uma Clínica Veterinária com atendimento 24 horas
"""  # Estrutura de comentário com informações inicias

""" Funções 'def's usadas no código
"""

def validaEmail(email):
    if email.find('@') > 2:
        return email
    else:
        print('E-mail inválido.')
        email = (input('Por favor digite novamente: '))
        validaEmail(email)


def validaCPF(cpf):  # Função que lê o tanto de carcteres digitados e limita-se a aceitar apenas 11 em um laço
    while (len(str(cpf)) != 11):
        cpf = (int(input('CPF inválido. Por favor, digite novamente: ')))
    return cpf


def retornarOuSair():  # Função que dá a opção de retornar nas respostas das condicionais do menu 2
    global condicao1 
    global condicao2
    print('\nO que deseja fazer agora?')
    print('4 - Retornar ao início')
    print('5 - Encerrar atendimento')

    respostaRetornarOuSair = int(input('\nDigite a opção desejada de acordo com os números acima: '))

    if respostaRetornarOuSair == 4:
        condicao2 = False
    elif respostaRetornarOuSair == 5:
        print('\nAtendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
        condicao1 = False
        condicao2 = False
    else:
        print('Resposta Inválida')

        retornarOuSair()


""" Variáveis usadas no código
"""
condicao1 = True  # Variável condicional usada no while para parar o loop quando o user quiser sair do programa em geral
condicao2 = True  # Variável condicional usada no segundo menu para parar o loop

menu1 = 0  # Variável de atribuição do menu 1
menu2 = 0  # Variável de atribuição do menu 2

# ----------------------------- IDENTIFICAÇÃO DO USUÁRIO ---------------------------------

print("Seja bem-vindo ao atendimento do Santuário dos Animais!")
nome = input('\nPara começar, qual o seu nome? ')
cpf = input(
    f'Obrigado, {nome}! Por favor, digite agora o seu CPF (sem pontos ou traços): ')
cpf = validaCPF(cpf)
email = input('Excelente! E qual o seu melhor e-mail? ')
email = validaEmail(email)
# --------------------------------- MENU INICIAL------------------------------

while condicao1:  # Laço de repeição, onde se a variável for diferente de Falso fica em loop

    condicao2 = True  # Atribuição do valor True para a variável condicao devido ao retorno ao menu que torna a variável como False

    # Menu de opcões do chatbot em loop

    # Utiliza o f, para apresentar uma variável no print
    print(f'\nEstamos prontos para cuidar do seu pet, {nome}!')
    # Utiliza o \n para pular uma linha da anterior, para organização do código
    print('\n1 - Para acessar a emergência')
    print('2 - Para acessar a área de exames')
    print('3 - Para acessar o financeiro')
    print('4 - Para acessar a área de consultas')
    print('5 - Para acessar as informações de contato')
    print('6 - Encerrar o atendimento')

    menu1 = int(
        input('\nPor favor, digite a opção desejada de acordo com os números acima: '))

# ----------------------------------- EMERGÊNCIA ---------------------------------------------
    if menu1 == 1:

        while condicao2:

            # Menu de segundo nível

            print(f'\nSeja bem vindo(a) a emergência {nome}!')
            print('\n1 - Sou cliente conveniado. ')
            print('2 - Não sou cliente conveniado')
            print('3 - Como cuidar do meu pet até o atendimento.')
            print('4 - Retornar ao início')
            print('5 - Encerrar atendimento')

            menu2 = int(
                input('\nPor favor, digite a opção desejada de acordo com os números acima: '))

            # Estrutura de condicionais para as opcões do menu de segundo nível

            if menu2 == 1:
                print(
                    '\nPor favor, ligue para: (11) 3572-9850. Estamos disponíveis 24 horas, todos os dias da semana.')
                retornarOuSair()
            elif menu2 == 2:
                print(
                    '\nPor favor, ligue para: (11) 3572-9851. Estamos disponíveis 24 horas, todos os dias da semana.')
                retornarOuSair()
            elif menu2 == 3:
                print("\nO veterinário(a) está a caminho! Por favor, mantenha a calma e acesse https://bit.ly/3zKKh0u para saber como proceder se o seu pet apresenta sinais de: \n*engasgamento \n*queimaduras \n*fraturas internas e/ou externas \n*intoxicação ou envenenamento \n*cortes e hemorragia")
                retornarOuSair()
            elif menu2 == 4:
                print('\nVocê será redirecionado ao nosso menu')
                condicao2 = False
            elif menu2 == 5:
                print(
                    '\nAtendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
                condicao1 = False
                condicao2 = False
            else:
                print('\nEssa não é uma opção válida. Por favor tente novamente.')

# ---------------------------------------EXAMES----------------------------------------------
    elif menu1 == 2:

        while condicao2:

            # Menu de segundo nível

            print(f'\nSeja bem vindo(a) a área de exames {nome}!')
            print('\n1 - Preparação para exames')
            print('2 - Marcação de exames')
            print('3 - Solicitação de Resultado')
            print('4 - Retornar ao início')
            print('5 - Encerrar atendimento')

            menu2 = int(
                input('\nPor favor, digite a opção desejada de acordo com os números acima: '))

            # Estrutura de condicionais para as opcões do menu de segundo nível

            if menu2 == 1:
                print('\nPara exame de sangue padrão: jejum alimentar de 8 horas e água à vontade.\nPara exame de urina: evitar que o seu pet urine por no mínimo 2 horas antes do exame. \nPara exame de fezes: não há preparo necessário, o tutor deve utilizar coletor universal para recolher as fezes.\nPara demais exames: acesse: https://bit.ly/3OpMItp')
                retornarOuSair()
            elif menu2 == 2:
                print(
                    '\nPor favor, ligue para: (11) 3572 - 9853) - Estamos disponíveis de segunda à sexta-feira das 8:00 às 18:00.')
                retornarOuSair()
            elif menu2 == 3:
                print(
                    f'\nOs resultados de exames encontrados do seu(s) pet(s) foram enviados para o e-mail: {email}')
                retornarOuSair()
            elif menu2 == 4:
                print('\nVocê será redirecionado ao nosso menu')
                condicao2 = False
            elif menu2 == 5:
                print(
                    '\Atendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
                condicao1 = False
                condicao2 = False
            else:
                print('\nEssa não é uma opção válida. Por favor tente novamente.')

# ---------------------------------------FINANCEIRO----------------------------------------------
    elif menu1 == 3:

        while condicao2:

            # Menu de segundo nível

            print(f'\nSeja bem vindo(a) ao financeiro {nome}!')
            print('1 - Planos')
            print('2 - Opções de pagamento')
            print('3 - Cliente conveniado: alterar a data de vencimento')
            print('4 - Retornar ao início')
            print('5 - Encerrar atendimento')

            menu2 = int(
                input('\nPor favor, digite a opção desejada de acordo com os números acima: '))

            # Estrutura de condicionais para as opcões do menu de segundo nível

            if menu2 == 1:
                print('\nPlano Mensal: R$ 94,90')
                print('Plano Semestral: R$ 498,90')
                print('Plano Anual: R$ 915,90')
                print(
                    'Por favor, ligue para (11) 3572-9854 e entenda melhor todos os benefícios oferecidos em cada plano!')
                retornarOuSair()
            elif menu2 == 2:
                print('Aceitamos as seguintes formas de pagamento:')
                print('\nPIX')
                print('Boleto')
                print('Cartão de Débito')
                print('Cartão de Crédito - até 10 vezes, sem juros.')
                retornarOuSair()
            elif menu2 == 3:
                print('\nDatas disponíveis: 5, 10, 15, 20, 25. \nPor favor, ligue para: (11) 3572-9854 para confirmar a alteração. Estamos disponíveis de segunda à sexta-feira das 8:00 às 18:00.')
                retornarOuSair()
            elif menu2 == 4:
                print('\nVocê será redirecionado ao nosso menu')
                condicao2 = False
            elif menu2 == 5:
                print(
                    '\nAtendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
                condicao1 = False
                condicao2 = False
            else:
                print('\nEssa não é uma opção válida. Por favor tente novamente.')

# -------------------------- CONSULTAS/ESPECIALIDADE -------------------------------------------
    elif menu1 == 4:

        while condicao2:

            # Menu de segundo nível

            print(f'\nSeja bem-vindo(a) à área de Consultas, {nome}!')
            print(f'\n1 - Especialidades Disponíveis')
            print('2 - Marcação de Consulta')
            print('3 - Direito ao Retorno')
            print('4 - Retornar ao início')
            print('5 - Encerrar atendimento')

            menu2 = int(
                input(f'\nPor favor, digite a opção desejada de acordo com os números acima: '))

            # Estrutura de condicionais para as opcões do menu de segundo nível

            if menu2 == 1:
                print(f'\nOferecemos o melhor atendimento em: \nClínica Geral – Dr. João Siqueira (CRMV-SP4413) | Dra. Fabiana Melo (CRMV-SP1109)| Dra. Lucia Santiago (CRMV-MG1305)\nCirurgia Geral – Dr. João Siqueira (CRMV-SP4413) | Dra. Lucia Santiago (CRMV-MG1305) \nE muitas outras especialidades! Por favor, acesse o link para saber mais: https://bit.ly/3QtsWz2')
                retornarOuSair()
            elif menu2 == 2:
                print(
                    f'\nPor favor, ligue para: (11) 3572-9855.Estamos disponíveis de segunda à sexta-feira das 8:00h às 18:00h.')
                retornarOuSair()
            elif menu2 == 3:
                print(f'\nO seu pet tem direito a um (1) retorno gratuito disponível em até 30 dias após a data da última consulta. \nPara confirmar, por favor ligue para : (11) 3572-9855.Estamos disponíveis de segunda à sexta-feira das 08:00h às 18:00h.')
                retornarOuSair()
            elif menu2 == 4:
                print(f'\nVocê será redirecionado ao nosso menu')
                condicao2 = False
            elif menu2 == 5:
                print(
                    f'\nAtendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
                condicao1 = False
                condicao2 = False
            else:
                print('\nEssa não é uma opção válida. Por favor tente novamente.')

# ----------------------------------- CONTATOS -------------------------------------------------
    elif menu1 == 5:

        while condicao2:

            # Menu de segundo nível

            print(
                f'\nSeja bem vindo(a) à área de Informações de Contato, {nome}!')

            print('\n1 - Contato')
            print('2 - Endereço')
            print('3 - Redes Sociais')
            print('4 - Falar com o(a) atendente')
            print('5 - Retornar ao início')
            print('6 - Encerrar o atendimento')

            menu2 = int(
                input('\nPor favor, digite a opção desejada de acordo com os números acima: '))

            # Estrutura de condicionais para as opcões do menu de segundo nível

            if menu2 == 1:
                print('\nVocê pode nos encontrar em:')
                print(
                    'Telefone: (11) 3572-9856\nWhatsapp: (11) 91135 - 9858\nE-mail: contato@santuariodosanimais.com')
                retornarOuSair()
            elif menu2 == 2:
                print('\nVocê pode nos encontrar em:')
                print(
                    'Rua das Laranjeiras, 123 - Alto da Lapa - Zona Oeste - São Paulo/SP')
                print('A clínica está localizada próxima as regiões da Lapa, Pinheiros, Alto de Pinheiros, Vila Leopoldina e Vila Madalena.')
                retornarOuSair()
            elif menu2 == 3:
                print('\nAcesse nossas redes sociais: ')
                print('Instagram: https://instagram.com/SantuariodosAnimais')
                print('Facebook: https://facebook.com/SantuariodosAnimais')
                retornarOuSair()
            elif menu2 == 4:
                print(
                    '\nVocê selecionou falar com o(a) atendente. Por favor, clique no link a seguir:')
                # Link de um direcionador para o chat com a atendente com um encurtador do link
                print('https://bit.ly/3NWa7L')
                retornarOuSair()
            elif menu2 == 5:
                print('\nVocê será redirecionado ao nosso menu')
                condicao2 = False
            elif menu2 == 6:
                print(
                    '\Atendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
                condicao1 = False
                condicao2 = False
            else:
                print('\nEssa não é uma opção válida. Por favor tente novamente.')

# ---------------------------------------- ENCERRAR ------------------------------------------------
    # Encerramento do atendimento, mudando a condicao para False e saindo do loop

    elif menu1 == 6:
        print('\nAtendimento finalizado, é sempre um prazer receber nossos aumigos e gatoamigos!')
        condicao1 = False

    # Se não for digitado uma opção dentre as mostradas entra no else, dá uma mensagem de erro e repete o menu

    else:
        print('\nEssa não é uma opção válida. Por favor, tente novamente.')
