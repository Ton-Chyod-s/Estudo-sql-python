import mysql.connector

#CRUD em Python - Python e MySQL - youtube.com

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'bdyoutube',
)
cursor =  conexao.cursor()

#create

comando = 'INSERT INTO'
cursor.execute(comando)
conexao.commit()

resultado = cursor.fetchall()


cursor.close()
conexao.close()