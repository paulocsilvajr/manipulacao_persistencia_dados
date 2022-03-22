import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DB:
    def __init__(self, host: str, banco: str, usuario: str, senha: str, porta: int):
        self.conexao = psycopg2.connect(host=host,
                                        database=banco,
                                        user=usuario,
                                        password=senha,
                                        port=porta)
        self.conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    def executar_sql(self, sql: str) -> str:
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
        except (Exception, psycopg2.DatabaseError) as error:
            return f'Error: {error}'

    def __del__(self):
        self.conexao.close()
