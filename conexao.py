import sqlite3

conexao = sqlite3.connect('db')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(90), idade INT, curso VARCHAR(90))');

#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (1, "ANTONIO SILVA", 34, "DIREITO")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (1, "AMANDA SANCHES", 25, "ENGENHARIA")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (1, "BIANCA COSTA", 40, "ENFERMAGEM")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (1, "DANILO CABRAL", 44, "ECONOMIA")')
#cursor.execute('INSERT INTO alunos(id,nome, idade, curso) VALUES (1, "HELOISA FONTES", 34, "DATA SCIENCE")')

# consultar = cursor.execute('SELECT * FROM alunos')
# for alunos in consultar:
#    print(alunos)

# consultar = cursor.execute('SELECT nome FROM alunos WHERE idade> 39')  
# for alunos in consultar: 
#   print(alunos) 

# consultar = cursor.execute('SELECT * FROM alunos WHERE curso == "ENGENHARIA"')  
# for alunos in consultar: 
#   print(alunos) 


#'SELECT * FROM alunos COUNT 




conexao.commit()
conexao.close()
