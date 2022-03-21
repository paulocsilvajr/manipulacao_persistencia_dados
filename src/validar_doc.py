from validate_docbr import CPF, CNPJ


class ValidarDOC():
    def __init__(self, lista: list):
        self._lista = lista
        self._cpf = CPF()
        self._cnpj = CNPJ()

    def validar(self):
        for item in self._lista:
            validacao = self._verificador(item[0])
            if not validacao(item[0]):
                print(item[0])

    def _verificador(self, identificador):
        if len(identificador) <= 14:
            return self._cpf.validate
        return self._cnpj.validate
