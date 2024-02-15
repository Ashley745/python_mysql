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