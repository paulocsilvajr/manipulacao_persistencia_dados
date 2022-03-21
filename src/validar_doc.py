from validate_docbr import CPF, CNPJ


class ValidarDOC:
    def __init__(self, lista: list):
        self._lista = lista
        self._cpf = CPF()
        self._cnpj = CNPJ()

    def validar(self) -> list:
        lista_doc_invalido = list()
        for item in self._lista:
            validacao = self._verificador(item[0])
            if not validacao(item[0]):
                lista_doc_invalido.append(item[0])

        return lista_doc_invalido

    def _verificador(self, identificador):
        if len(identificador) <= 14:
            return self._cpf.validate
        return self._cnpj.validate
