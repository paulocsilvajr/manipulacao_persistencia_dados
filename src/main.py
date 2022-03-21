import sys
from separador import Separador
from validar_doc import ValidarDOC

arquivo = sys.argv[1]

with open(arquivo) as f:
    texto = f.readlines()

sep = Separador(texto)
dados = sep.retornar_elementos_em_lista()
print(dados[0])

valcpf = ValidarDOC(dados[1:])
valcpf.validar()


