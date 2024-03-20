import sqlite3

#conectar
conn = sqlite3.connect("exemplo.db")

#criando um cursor para executar o comando em sql 
cursor = conn.cursor()

#Criar tabela pessoas
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
                (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')

#Inserir Dados
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?,?)",('João',25))
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?,?)",('Maria',30))
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?,?)",('Ana',22))
conn.commit()

#Selecionar e exibir dados
cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

for pessoas in pessoas:
    print(pessoas)

#Fecha Conexão
conn.close()