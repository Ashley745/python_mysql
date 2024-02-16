import mysql.connector as mc

# estabelecer a conexão com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# verificar se a conexão foi estabelecida
print(cx)

# criação de variáveis para o usuário passar os dados do cliente
# para cadastrar
nome = input("Digite o nome do cliente: ")
email = input("Digite o emaildo cliente: ")
telefone= input("Digite o telefone do cliente: ")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# confirmar a inserção dos dados na tabela
print(cx.commit())


