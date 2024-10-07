import mysql.connector
from jinja2 import Environment, FileSystemLoader

# Função para buscar os resultados no banco de dados
# Este programa será configurado para executar de hora em hora
 
mydb = mysql.connector.connect(
  host="host",
  user="usuario",
  password="senha",
  database="banco"
)

mycursor = mydb.cursor()
mycursor.execute(
    """SELECT tipo, tamanho, sex, instituicao, cidade, condicao, quantidade 
    FROM doacoes dc
    left join escolas es on escolas.instituicao = doacoes.instituicao"
    where dc.entregue <>'ok'
"""    
)
myresult = mycursor.fetchall()


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template_listagem.html')
template_vars = {'doacoes': myresult}

# Renderizar o template e salvar o resultado em um novo arquivo HTML
with open('listagem.html', 'w') as f:
    f.write(template.render(template_vars))

#print("Arquivo resultado.html gerado com sucesso!")