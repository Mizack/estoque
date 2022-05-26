import pyodbc

class Banco:
    def __init__(self) -> None:
        self.conexao,self.cursor = self.chamar_db()

    def chamar_db(self):
        try: # Conectar com o banco de dados
            server = 'DESKTOP-2DECLDH' 
            database = 'ESTOQUE' 
            conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
            cursor = conexao.cursor()
            print("Conectado com sucesso!")
            return conexao,cursor
        except: 
            print("Conexão falhou")
            return False