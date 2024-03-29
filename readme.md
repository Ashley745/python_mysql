# Conexão do Python com o MySQL

!["Imagem Python com MySQL"](https://miro.medium.com/v2/resize:fit:1358/1*5PSjhz9Xx-4cj4Dz2FrHkA.jpeg)

## Drive de comunicação com o MySQL
Para estabalecer s comunicação entre o Python e
 o banco de dados MySql, iremos usar o  seguinte drive
<a href="https://pypi.org/project/mysql-connector-python/#description"> https://pypi.org/project/mysql-connector-python/#description </a>

### Comando para instalar o drive
```python
    python -m pip install mysql-connector-python
```

### Configuração banco de dados MySQL
O noso banco de dados está em um container de docker. Para acessá-lo será necessário o container, então faremos os seguintes comandos em um servidor Fedora com docker instlado:

#### Criação do volume
```shell
mkdir dadosclientes
```

#### Criação do container
<center>
<img src="https://cdn.iconscout.com/icon/free/png-256/free-docker-226091.png" height="100" width="100">
</center>

```shell
    docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQl_ROOT_PASSW0RD=senac@123 -d mysql
```

### Criação do banco ded ados da tabela clientes

```sql
create database banco;
use banco;
create table clientes(
clientes_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar (100) not null unique,
telefone varchar(20)
)
```

### Arquivo clientes.py

```
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

```

#### Arquivo de cadastro: cad-clientes.py

```python

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

```

#### Arquivo de atualização: up_clientes.py

```python
import mysql.connector as mc
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()
cursor.execute("Select * from clientes")
for i in cursor:
    print(i)

print("O que você deseja atualizar, digite:")
print("1 - para Nome")
print("2 - para E-mail")
print("3 - para telefone")
op = input("Digite a opção desejada: ")
id = input("Agora digite o id do cliente: ")
dado = input("Digite a nova infromação: ")
if(op=="1"):
    cursor.execute("update clientes set nome_cliente='"+dado+"' where clientes_id="+id)
elif(op=="2"):
    cursor.execute("update clientes set email='"+dado+"' where clientes_id="+id)
elif(op=="3"):
    cursor.execute("update clientes set telefone='"+dado+"' where clientes_id="+id)
else:
    print("Opção inválida!")

cx.commit()
```

#### Criação do arquivo del_clientes.py

```python
import mysql.connector as mc

con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

os.system("cls")
cursor = con.cursor()
cursor.execute("Select * from clientes")
for c in cursor:
    print(c)

id = input("Digite o id do cliente que deseja apagar: ")
rs = input("Você realmete deseja apagar esse cliente? Digite (s ou n):")
if(rs=="s" or rs=="S"):
    cursor.execute("delete from clientes where clientes_id="+id)
    con.commit()
else:
    print("--------- Opção inválida ----------")
```