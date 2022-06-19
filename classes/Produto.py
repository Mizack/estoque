import sys
sys.path.append(".")
from classes.Validacoes import Validacoes
class Produto:
    
    def __init__(self,nome:str="",valor:float="",descricao:str="",quantidade:int="",codigo:int=0):
        self.lista_erros = []
        self.validacoes = Validacoes()

        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.quantidade = quantidade
        if codigo != 0:
            self.codigo = codigo


    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo:int):
        if self.__validar_campo_vazio(codigo):
            self._codigo = codigo
        else:
            self.inserir_erro("Erro na validação de codigo")


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if self.__validar_campo_vazio(nome):
            self._nome = nome
        else:
            self.inserir_erro("Erro na validação de nome")


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if self.__validar_campo_vazio(valor):
            self._valor = valor
        else:
            self.inserir_erro("Erro na validação de valor")


    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        if self.__validar_campo_vazio(descricao):
            self._descricao = descricao
        else:
            self.inserir_erro("Erro na validação de descricao")


    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if self.__validar_campo_vazio(quantidade):
            self._quantidade = quantidade
        else:
            self.inserir_erro("Erro na validação de quantidade")


    def erro_instancia(self):
        if self.__validar_campo_vazio(self.lista_erros):
            return self.validacoes.gerar_codigo_status(400,self.lista_erros)
        else:
            return True

    def inserir_erro(self,lista_erros):
        self.lista_erros.append(lista_erros)

    def retornar_dados_insercao(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade)
        return [dados]
    
    def retornar_dados_alterar(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade,self.codigo)
        return [dados]

    def __validar_campo_vazio(self,campo)->bool:
        if campo == "" or campo == None or not campo:
            return False
        else:
            return True