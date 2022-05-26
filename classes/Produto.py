from classes.Banco import Banco
class Produto:
    def __init__(self) -> None:
        self.banco = Banco()

    def construtor(self,nome:str,valor:float,descricao:str,quantidade:int,codigo:int=0,) -> None:
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.quantidade = quantidade

    def listar_produtos(self):
        try:
            sql = 'SELECT * FROM TB_PRODUTO'
            self.banco.cursor.execute(sql)
            resultado = self.banco.cursor.fetchall()
            return self.listagem(resultado)
        except:
            print('erro de conexão')
            return False

    def listagem(self,resultado):
        json_retornado = []
        for dados_retornados in resultado:
            sub_json = {
                'codigo':dados_retornados[0],
                'nome':dados_retornados[1],
                'valor':dados_retornados[2],
                'descricao':dados_retornados[3],
                'quantidade':dados_retornados[4],
                'ultima_alteracao':dados_retornados[5]
            }
            json_retornado.append(sub_json)
        return json_retornado