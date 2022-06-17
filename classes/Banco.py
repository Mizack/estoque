import pymysql
import os
from dotenv import load_dotenv


class Banco:
    def __init__(self) -> None:
        self.conexao,self.cursor = self.__chamar_db()

    def __chamar_db(self):
        try: # Conectar com o banco de dados
            load_dotenv()
            endpoint= os.environ.get("endpoint")
            user= os.environ.get("user")
            psswd= os.environ.get("psswd")
            conexao = pymysql.connect(host= endpoint,user= user,password= psswd,database="estoque")
            cursor = conexao.cursor()
            return conexao,cursor
        except: 
            print("Conexão falhou")
            return False # colocar um json como retorno

    # def __buscar_dado(self)