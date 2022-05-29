class Produto:

    def __init__(self,nome:str,valor:float,descricao:str,quantidade:int,codigo:int=0,) -> None:
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.quantidade = quantidade

    def retornar_dados_insercao(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade)
        return [dados]
    
    def retornar_dados_alterar(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade,self.codigo)
        return [dados]