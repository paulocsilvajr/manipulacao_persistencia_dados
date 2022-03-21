class Separador():
    def __init__(self, arquivo: str):
        self.arquivo = arquivo

        self._sep_cpf = slice(0, 19)
        self._sep_private = slice(19, 31)
        self._sep_imcompleto = slice(31, 43)
        self._sep_data_ultima_compra = slice(43, 65)
        self._sep_ticket_medio = slice(65, 87)
        self._sep_ticket_ultima_compra = slice(87, 111)
        self._sep_loja_mais_frequente = slice(111, 131)
        self._sep_loja_ultima_compra = slice(131, 152)

    def retornar_elementos_em_lista(self) -> list:
        lista = list()
        for linha in self.arquivo:
            lista.append(self._separar_elementos(linha))

        return lista

    def _separar_elementos(self, linha) -> tuple:
        return (self._remover_espacos(linha[self._sep_cpf]),
                self._remover_espacos(linha[self._sep_private]),
                self._remover_espacos(linha[self._sep_imcompleto]),
                self._remover_espacos(linha[self._sep_data_ultima_compra]),
                self._remover_espacos(linha[self._sep_ticket_medio]),
                self._remover_espacos(linha[self._sep_ticket_ultima_compra]),
                self._remover_espacos(linha[self._sep_loja_mais_frequente]),
                self._remover_espacos(linha[self._sep_loja_ultima_compra]))

    def _remover_espacos(self, texto: str) -> str:
        return texto.strip()
