import sys
from separador import Separador

arquivo = sys.argv[1]

with open(arquivo) as f:
    texto = f.readlines()

sep = Separador(texto)
print(sep.retornar_elementos_em_lista()[0])



