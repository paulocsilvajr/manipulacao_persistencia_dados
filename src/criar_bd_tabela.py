from db import DB


def criar_db_tabela(host: str, porta: int):
    db = DB(host, 'postgres', 'postgres', 'postgres', porta)
    db.executar_sql('CREATE DATABASE banco_consulting_services;')
    del db

    db = DB(host, 'banco_consulting_services', 'postgres', 'postgres', porta)
    db.executar_sql('''
    CREATE TABLE IF NOT EXISTS dados(
        cpf varchar(18) NOT NULL,
        private boolean NOT NULL,
        incompleto boolean NOT NULL,
        data_ultima_compra date NULL,
        ticket_medio money NULL,
        ticket_ultima_compra money NULL,
        loja_mais_frequente varchar(18) NULL,
        loja_ultima_compra varchar(18) NULL)''')
    del db
