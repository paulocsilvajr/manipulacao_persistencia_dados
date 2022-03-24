# Manipulação e persistência de dados
## Aplicação desenvolvida para gravar informações de arquivo base(txt) em Banco de Dados PostgreSQL via containers Docker

Este repositório contém arquivos para efetuar a gravação de registros oriundos de um arquivo(base_teste (1).txt) para uma base de dados PostgreSQL. Todas as funcionalidades estão escapsuladas dentro de dois containers separados, um para a aplicação Python e outro para o Banco PostgreSQL. A partir do docker-compose, é feito a gravação automática desses dados

### Instruções

Para rodar essa aplicação, é necessário estar disponível o Docker e o Docker-compose, disponíveis pelo link [Docker](https://docs.docker.com/desktop/windows/install/) ou a partir dos repositórios padrão de distribuições Linux baseadas no Ubuntu 18.04 ou superior.

Para executar a tarefa de gravação dos dados é necessário executar o seguinte comando:
```
docker-compose up --build -d
```
Será criado os containers 'manipulacao_persistencia_dados_python-compose_1' e 'manipulacao_persistencia_dados_postgres-compose_1' e efetuado a inserção dos registros de arquivo 'base_teste (1).txt' para o PostgreSQL rodando no container.

O container 'manipulacao_persistencia_dados_python-compose_1' é finalizado automaticamente ao finalizar gravação dos registros.

Execute o comando abaixo para derrubar os serviços:
```
docker-compose down
```

### Arquivos
```
README.md: Este arquivo de ajuda.
dockerfile: Arquivo que contém informações para a criação de imagem do Docker base para rodar a aplicação de gravação em Python
docker-compose.yml: Arquivo contém as instruções para a criação dos dois container Docker: PostgreSQL e Python, baseado em imagen criada a partir de dockerfile
base_teste (1).txt: Arquivo base contendo os registros que serão gravados no banco de dados PostgreSQL
.gitignore: Arquivo do GIT que contém descrição dos arquivos/pastas que serão ignoradas pelo repositório
src/main.py: Arquivo principal do projeto, onde é executado as tarefas leitura do arquivo base e a criação de Banco de Dados e Tabela e gravação dos registros em container PostgreSQL
src/requeriments.txt: Arquivo com as dependências do projeto Python, instalados via PIP
src/separador.py: Arquivo com classe separadora de elementos para o arquivo base em texto
src/validar_doc.py: Arquivo com classe validadora de documentos(CPF e CNPJ)
src/db.py: Arquivo com classe para a conexão e manipulação de banco PostgreSQL via psycopg
src/criar_db_tabela.py: Arquivo com o processo de criação do banco 'banco_consulting_services' e da tabela 'dados'
src/inserir_registros.py: Arquivo com os passos para a inserção das dados capturados no arquivo base 'base_teste (1).txt'
```


### Contato

Paulo Carvalho da Silva Junior - pauluscave@gmail.com
