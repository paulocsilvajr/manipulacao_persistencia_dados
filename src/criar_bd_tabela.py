from db import DB


def criar_db_tabela():
    # db = DB('manipulacao_persistencia_dados_postgres-compose_1', 'postgres', 'postgres', 'postgres', 5432)
    db = DB('localhost', 'postgres', 'postgres', 'postgres', 15432)
    db.executar_sql('CREATE DATABASE banco_consulting_services;')
    del db

    # db = DB('manipulacao_persistencia_dados_postgres-compose_1', 'banco_consulting_services', 'postgres', 'postgres', 5432)
    db = DB('localhost', 'banco_consulting_services', 'postgres', 'postgres', 15432)
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
