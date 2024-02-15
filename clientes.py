# importando a biblioteca de conexão com o banco de dados
# nmysql
# vamos adicionar um alias a biblioteca

import mysql.connector as mc
# vamos estabelecer a conexão com o banco 
# de dados e para tal, iremos passsar os 
# seguintes dados: 
# servidor,porta,usuario,senha,banco

conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

# Estamos testando a conexão pedindo para
# exibir a id da conexão. Caso exiba uma
# pilha de erros então você tem um erro
# na linha de conexão
print(conexao)

# Para se movimentar dentro da estrututra de
#banco de dados e retornar dos dados necessários
# iremos criar cursor
cursor = conexao.cursor()

# Vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")

# cursor.execute("insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@yahoo.com.br','(54) 9985-6854')")

# Vamos selecionar todos os dados da tabela clientes
rs = cursor.execute("Select * from banco.clientes")
print(cursor)
for c in cursor:
    print(f"Id do Cliente: {c[0]}")
    print(f"Nome do Cliente: {c[1]}")
    print(f"E-mail: {c[2]}")