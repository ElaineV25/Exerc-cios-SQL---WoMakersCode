import sqlite3

conexao = sqlite3.connect('db')
cursor = conexao.cursor()

#Exercício 1

#cursor.execute('CREATE TABLE alunos(id INT PRIMARY KEY, nome VARCHAR(90), idade INT, curso VARCHAR(90))')

#Exercício 2

#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (1, "ANTONIO SILVA", 34, "DIREITO")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (2, "DANILO CABRAL", 44, "ECONOMIA")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (3, "AMANDA SANCHES", 25, "ENGENHARIA")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (4, "BIANCA COSTA", 40, "ENFERMAGEM")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (5, "HELOISA FONTES", 34, "DATA SCIENCE")')

#Exercício 3

# consultar = cursor.execute('SELECT * FROM alunos')
# for alunos in consultar:
#    print(alunos)

# consultar = cursor.execute('SELECT nome FROM alunos WHERE idade> 39')  
# for alunos in consultar: 
#   print(alunos) 

# consultar = cursor.execute('SELECT * FROM alunos WHERE curso == "ENGENHARIA"')  
# for alunos in consultar: 
#   print(alunos) 


#cursor.execute('SELECT COUNT (*) FROM alunos')

#Exercício 4
#cursor.execute('UPDATE alunos SET idade = 21 WHERE  nome = "DANILO CABRAL"')

#cursor.execute('DELETE FROM alunos WHERE id = 1')

#Exercício 5

# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(90), idade INT, saldo FLOAT(10))')
# cursor.execute('INSERT INTO clientes(id,nome, idade, saldo) VALUES (1, "VALQUIRIA SOUZA", 39, "900.00")')
# cursor.execute('INSERT INTO clientes(id,nome, idade, saldo) VALUES (2, "LUIZ CRUZ", 26, "450.00")')
# cursor.execute('INSERT INTO clientes(id,nome, idade, saldo) VALUES (3, "CLARICE ALVES", 20, "65.00")')
# cursor.execute('INSERT INTO clientes(id,nome, idade, saldo) VALUES (4, "GUSTAVO DIAS", 45, "660.00")')
# cursor.execute('INSERT INTO clientes(id,nome, idade, saldo) VALUES (5, "ALANA MEDEIROS", 45, "6570.00")')
# cursor.execute('INSERT INTO clientes(id,nome, idade, saldo) VALUES (6, "DENISE RIBEIRO", 22, "150.00")')


#Exercício 6

# idade = cursor.execute('SELECT nome FROM clientes WHERE idade> 30')  
# for clientes in idade: 
#   print(clientes) 


# saldo_medio = cursor.execute('SELECT AVG (saldo) FROM clientes GROUP BY id')
# for clientes in saldo_medio: 
#  print(saldo_medio) 


# saldo_maior = cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC')  
# for clientes in saldo_maior: 
#   print(clientes) 


# saldo = cursor.execute('SELECT COUNT (*) FROM clientes WHERE saldo > 1000')
# for clientes in saldo: 
#  print(saldo) 

#Exercício 7

#cursor.execute('UPDATE clientes SET saldo = 25000 WHERE  nome = "CLARICE ALVES"')
#cursor.execute('DELETE FROM clientes WHERE id = 6')


#Exercício 8

#cursor.execute('drop table compras ')

#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id, produto VARCHAR(60), valor REAL(10))')

#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 5, "TV", "750.00")')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 4, "FOGÃO", "440.00")')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 1, "CELULAR", "500.00")')

dados = cursor.execute('SELECT nome, produto , valor FROM clientes INNER JOIN compras ON clientes.id = compras.id ')  
for clientes in dados:
   print(clientes)




conexao.commit()
conexao.close()
