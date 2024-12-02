import psycopg2
from psycopg2 import sql

class Database: # Cria objeto que faz conexão com o bd
    def __init__(self, db_name, user, password, host='localhost', port=5432):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor() # O objeto cursor é responsável pelas consultas ao banco

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params) # query = consulta| params = parametros
            self.connection.commit() # Salva alteracao no banco
        except Exception as e:
            self.connection.rollback() # Desfaz uma alteração feita
            print(f"Error executing query: {e}")
    
    def fetchall(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall() # Retornar os registros obtidos pela consulta
    
    def close(self): # Encerra a conexao com bd
        self.cursor.close()
        self.connection.close()
