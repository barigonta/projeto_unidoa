
import mysql.connector

# Função para gravar no banco de dados 
# Deve ser criado o banco e a tabela antes de executar esta função!!!

#Dados de conexão
mydb = mysql.connector.connect(
    host="host",
    user="usuario",
    password="senha",
    database="banco"
)
mycursor = mydb.cursor()

def inserir_doacao(instituicao, endereco, cidade, estado, contato, email, telefone):
    sql = """INSERT INTO escolas (
                 concat(Upper(substr(instituicao, 1,1)), lower(substr(instituicao, 2,length(instituicao)))) as instituicao, 
                 concat(Upper(substr(endereco, 1,1)), lower(substr(endereco, 2,length(endereco)))) as endereco, 
                 concat(Upper(substr(cidade, 1,1)), lower(substr(cidade, 2,length(cidade)))) as cidade, 
                 Upper(estado) as estado, 
                 concat(Upper(substr(contato, 1,1)), lower(substr(contato, 2,length(contato)))) as contato, 
                 lower(email) as email, 
                 telefone
                 ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    val = (instituicao, endereco, cidade, estado, contato, email, telefone)
    mycursor.execute(sql, val)
    mydb.commit()

# Exemplo de chamada da função 
#inserir_doacao("Escola ABC", "Rua da Escola", "Curitiba", "PR", "Fulano de Tal", "meuemail@teste.com", "4123456789")