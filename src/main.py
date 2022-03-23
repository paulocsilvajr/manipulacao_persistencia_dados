import sys
import time

from separador import Separador
from validar_doc import ValidarDOC
from criar_bd_tabela import criar_db_tabela
from inserir_registros import inserir_registros


def main():
    arquivo = sys.argv[1]

    with open(arquivo) as f:
        texto = f.readlines()

    sep = Separador(texto)
    dados = sep.retornar_elementos_em_lista()

    print('Colunas em arquivo base:', dados[0], sep='\n', end='\n\n')

    valcpf = ValidarDOC(dados[1:])
    lista_doc_invalido = valcpf.validar()
    if not lista_doc_invalido:
        print('NÃO hã CPF/CNPJ inválidos')
    else:
        print('Itens com CPF/CNPJ inválido', *lista_doc_invalido, sep='\n', end='\n\n')

    print('Esperando alguns segundos para inicializar container e serviço do PostgreSQL', end='\n\n')
    time.sleep(10)

    print("Criando banco 'banco_consulting_services' e tabela 'dados' para receber os dados de arquivo", end='\n\n')
    criar_db_tabela('manipulacao_persistencia_dados_postgres-compose_1', 5432)

    print(f'Gravando {len[dados[1:]]} registros em container PostgreSQL', end='\n\n')
    inserir_registros(dados[1:], 'manipulacao_persistencia_dados_postgres-compose_1', 5432)


if __name__ == '__main__':
    main()


