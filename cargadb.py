import psycopg2

def load_sql_file(filepath, db_params):

    # Conectando ao banco de dados
    conn = psycopg2.connect(
        host=db_params['host'],
        database=db_params['database'],
        user=db_params['user'],
        password=db_params['password']
    )

    conn.autocommit = True
    cursor = conn.cursor()

    # Lendo e executando o arquivo SQL
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.execute(sql_script)

    cursor.close()
    conn.close()
    print("Arquivo SQL carregado com sucesso!")

# Parâmetros de conexão
db_params = {
    'host': 'dpg-d0q74egdl3ps73bd11sg-a.oregon-postgres.render.com',
    'database': 'exemplo_db',
    'user': 'exemplo_db_user',
    'password': 'ea9Eb3aH8cCWL8rKqRPRQyOGlQjmWcrE'
}




# Caminho para o arquivo SQL
filepath = 'persons.sql'

# Carregando o arquivo
load_sql_file(filepath, db_params)
