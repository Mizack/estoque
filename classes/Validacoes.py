class Validacoes:

    def __init__(self) -> None:
        self.lista_erros = []
    
    def gerar_codigo_status(self,codigo:int,mensagem:str)->dict:
        codigo_status = {
            "codigo":codigo,
            "data":mensagem
        }
        return codigo_status

    def inserir_erro(self,lista_erros):
        self.lista_erros.append(lista_erros)