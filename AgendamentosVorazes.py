import sqlite3
import re

conn = sqlite3.connect("vorazes.db")
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS agendamento (
               id INTEGER PRIMARY KEY,
               cpf VARCHAR(50), 
               nome VARCHAR(50), 
               telefone VARCHAR(50), 
               email VARCHAR(50), 
               idade INTEGER, 
               sexo VARCHAR(50), 
               data_agendamento DATE, 
               especialidade VARCHAR(50)
               )''')

def incluirAgendamento():
    print('---Novo Agendamento---')
    cpf = input('Insira o CPF: ')
    nome = input('Insira o nome:')

    padrao_telefone = r'^\(\d{2}\)\d{5}-\d{4}$'
    telefone = ''
    while not re.match(padrao_telefone, telefone):
        telefone = input('Insira o telefone (XX)XXXXX-XXXX: ')

    padrao_email = r'^\w+[\w\.-]*@\w+[\w\.-]+\.\w+$'
    email = ''
    while not re.match(padrao_email, email):
        email = input('Insira o email: ')

    idade = int(input('Insira a idade: '))

    sexo = input('Insira o Sexo: ')

    padrao_data = r'^\d{2}/\d{2}/\d{4}$'
    data_agendamento = ''
    while not re.match(padrao_data, data_agendamento):
        data_agendamento = input('Insira a data do agendamento (DD/MM/YYYY): ')

    especialidade = input('Insira a especialidade: ')

    cursor.execute("INSERT INTO agendamento (cpf, nome, telefone, email, idade, sexo, data_agendamento, especialidade) VALUES (?,?,?,?,?,?,?,?)",
                   (cpf, nome, telefone, email, idade, sexo, data_agendamento, especialidade))
    conn.commit()

def listaAgendamento():
    cursor.execute("SELECT * FROM agendamento")
    agendamentos = cursor.fetchall()

    for agendamento in agendamentos:
        print(agendamento)

def excluirAgendamento():
    cpf_exclusao = input('Insira o CPF da pessoa que deseja excluir o agendamento: ')
    cursor.execute(f"DELETE FROM agendamento WHERE cpf = '{cpf_exclusao}'")
    conn.commit()

def validar_numero_inteiro(texto):
    while True:
        try:
            entrada = int(input(texto))
            break
        except ValueError:
            print("Erro: entrada inválida.")
    return entrada

menu = True  # Definindo a variável 'menu' aqui

while menu:
    print('Agendamentos')
    print('1. Incluir')
    print('2. Listar')
    print('3. Excluir')
    print('0. Sair')
    opcao = validar_numero_inteiro('Escolha uma opção: ')
    if opcao == 0:
        menu = False
    elif opcao == 1:
        incluirAgendamento()
    elif opcao == 2:
        listaAgendamento()
    elif opcao == 3:
        excluirAgendamento()
    else:
        print('Erro')

conn.close()
