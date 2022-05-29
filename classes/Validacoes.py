class Validacoes:
    def validar_chave_dict(self,dicionario,chave)->bool:
        if chave in dicionario:
            True
        else:
            False
    
    def gerar_codigo_status(self,codigo:int,mensagem:str)->dict:
        codigo_status = {
            "codigo":codigo,
            "mensagem":mensagem
        }
        return codigo_status