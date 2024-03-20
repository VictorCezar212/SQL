import sqlite3
import random
import time

conn = sqlite3.connect("allforone.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS teste
               (id INTEGER PRIMARY KEY, valor VARCHAR)''')

for i in range(1000000):
    valor = random.randint(1, 100)
    cursor.execute("INSERT INTO teste (valor) VALUES (?)", (valor,))
conn.commit()

def performance():
    start_time = time.time()  # Captura o tempo de início
    cursor.execute("SELECT * FROM teste WHERE valor BETWEEN 30 AND 70")
    end_time = time.time()    # Captura o tempo de fim
    print("Tempo de execução da consulta: {} segundos".format(end_time - start_time))

performance()

conn.close()
