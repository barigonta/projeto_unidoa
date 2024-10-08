
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

def inserir_doacao(nome, instituicao, data_entrega, tipo, tamanho, sex, quantidade, condicao):
    sql = """INSERT INTO doacoes (
            concat(Upper(substr(nome, 1,1)), lower(substr(nome, 2,length(nome)))) as nome, 
            instituicao, data_entrega, tipo, 
            concat(Upper(substr(tamanho, 1,1)), lower(substr(tamanho, 2,length(tamanho)))) as tamanho, 
            sex, quantidade, condicao
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    val = (nome, instituicao, data_entrega, tipo, tamanho, quantidade, condicao)
    mycursor.execute(sql, val)
    mydb.commit()

# Exemplo de chamada da função 
#inserir_doacao("João Silva", "Escola A", "2023-12-31", "Camisa", "M", 2, "Novo")
