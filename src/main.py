import sys
from separador import Separador
from validar_doc import ValidarDOC

def main():
    arquivo = sys.argv[1]

    with open(arquivo) as f:
        texto = f.readlines()

    sep = Separador(texto)
    dados = sep.retornar_elementos_em_lista()

    print(dados[0])

    valcpf = ValidarDOC(dados[1:])
    lista_doc_invalido = valcpf.validar()
    if not lista_doc_invalido:
        print('NÃO hã CPF/CNPJ inválidos')
    else:
        print('Itens com CPF/CNPJ inválido', *lista_doc_invalido, sep='\n')


if __name__ == '__main__':
    main()


