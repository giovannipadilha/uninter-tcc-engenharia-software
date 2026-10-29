# Clean Architecture em APIs RESTful

API RESTful desenvolvida em Python com aplicação dos princípios da Clean Architecture, como parte do Trabalho de Conclusão de Curso em Engenharia de Software da UNINTER.

O projeto tem como objetivo analisar a separação entre regras de negócio e detalhes de implementação, com foco na redução do acoplamento.

## Tecnologias

- Python
- FastAPI
- Pydantic
- SQLite

## Arquitetura

A aplicação está organizada em quatro camadas:

- **Entidades:** regras de negócio fundamentais.
- **Casos de uso:** criação e atualização de produtos.
- **Interface e adaptadores:** controladores e persistência.
- **Infraestrutura:** API e banco de dados.

## Execução

Crie e ative o ambiente virtual do Python:

`python3 -m venv .venv && source .venv/bin/activate`

Instale as dependências:

`pip install -r requirements.txt`

Inicie a aplicação a partir da raiz do projeto:

`fastapi dev src/main.py`

A documentação interativa estará disponível em:

`http://127.0.0.1:8000/docs`