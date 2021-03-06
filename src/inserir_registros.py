from db import DB


def inserir_registros(dados: list, host: str, porta: int):
    db = DB(host, 'banco_consulting_services', 'postgres', 'postgres', porta)
    for dado in dados:
        doc = converte_para_doc_formatado(dado[0])
        private = converte_para_boolean(dado[1])
        imcompleto = converte_para_boolean(dado[2])
        data_ultima_compra = converte_para_date(dado[3])
        ticket_medio = converte_para_float(dado[4])
        ticket_ultima_compra = converte_para_float(dado[5])
        loja_mais_frequente = converte_para_texto(dado[6])
        loja_ultima_compra = converte_para_texto(dado[7])

        sql = f'''
        INSERT INTO dados(
            cpf,
            private,
            incompleto,
            data_ultima_compra,
            ticket_medio,
            ticket_ultima_compra,
            loja_mais_frequente,
            loja_ultima_compra)
        VALUES(
            {doc},
            {private},
            {imcompleto},
            {data_ultima_compra},
            {ticket_medio},
            {ticket_ultima_compra},
            {loja_mais_frequente},
            {loja_ultima_compra})            
        '''

        retorno = db.executar_sql(sql)
        if retorno:
            print(retorno)

    del db


def converte_para_float(valor: str):
    if valor == 'NULL':
        return valor
    else:
        valor_convertido = valor.replace(',', '.')
        return float(valor_convertido)


def converte_para_boolean(valor: int):
    return 'true' if valor == 1 else 'false'


def converte_para_date(data: str):
    if data == 'NULL':
        return data
    else:
        return f"\'{data}\'"


def converte_para_texto(texto: str):
    if texto == 'NULL':
        return texto
    else:
        return f"\'{texto}\'"

def _formata_cpf(cpf: str) -> str:
        return f'{cpf[0-3]}.{cpf[3-6]}.{cpf[6-9]}-{cpf[9-11]}'


def converte_para_doc_formatado(identificador) -> str:
    cpf_sem_formatacao = len(identificador) == 11
    if cpf_sem_formatacao:
        identificador = _formata_cpf(identificador)
    
    return f"\'{identificador}\'"
