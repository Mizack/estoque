import pymysql

class Banco:
    def __init__(self) -> None:
        self.conexao,self.cursor = self.__chamar_db()

    def __chamar_db(self):
        try: # Conectar com o banco de dados

            endpoint= "miza.c4nf3gvviehu.us-east-1.rds.amazonaws.com"
            user= "admin"
            psswd= "Miza2214!" 
            conexao = pymysql.connect(host= endpoint,user= user,password= psswd,database="estoque")
            cursor = conexao.cursor()
            return conexao,cursor
        except: 
            print("Conexão falhou")
            return False # colocar um json como retorno

    # def __buscar_dado(self)