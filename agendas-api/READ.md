# Agendas API

API para gerenciamento de agendas desenvolvida com Django e Django REST Framework.

## Tecnologias Utilizadas

- Python 3.11
- Django 4.2
- Django REST Framework
- SQLite
- Docker

## Pré-requisitos

- Python 3.11+
- pip
- Docker e Docker Compose (opcional)

## Configuração e Execução

### Sem Docker

1. Clone o repositório

   ```bash
   git clone <url-do-repositorio>
   cd agendas-api
   ```
2. Criar e ativar ambiente virtual

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instalar dependências

   ```bash
   pip install -r requirements.txt
   ```
4. Aplicar migrações

   ```bash
   python manage.py migrate
   ```
5. Iniciar o servidor

   ```bash
   python manage.py runserver
   ```

### Com Docker

1. Clone o repositório
   ```bash
   git clone <url-do-repositorio>
   cd agendas-api
   ```
2. Construir e iniciar os containers
   ```bash
   docker-compose up -d
   ```
3. Acessar a API em [http://localhost:8000/api/](http://localhost:8000/api/)

## Endpoints da API

* `GET /api/agendas/` - Listar todas as agendas
* `POST /api/agendas/` - Criar uma nova agenda
* `GET /api/agendas/{id}/` - Obter detalhes de uma agenda
* `PUT /api/agendas/{id}/` - Atualizar uma agenda
* `PATCH /api/agendas/{id}/` - Atualizar parcialmente uma agenda
* `DELETE /api/agendas/{id}/` - Deletar uma agenda
* `PATCH /api/agendas/{id}/estado/` - Alterar o estado de uma agenda

### Exemplo de Payload para Criar/Atualizar Agenda

```json
{
  "titulo": "Reunião de Planejamento",
  "descricao": "Discussão sobre os próximos projetos",
  "dataInicio": "2023-10-20T14:00:00Z",
  "dataFim": "2023-10-20T16:00:00Z",
  "local": "Sala de Reuniões 2"
}
```

### Exemplo de Payload para Alterar Estado

```json
{
  "estado": "CONFIRMADO"
}
```

## Estados Possíveis

* RECEBIDO (padrão)
* CONFIRMADO
* ATENDIDO
* CANCELADO

## Documentação da API

A documentação da API está disponível através do Swagger UI:

* Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Estrutura do Projeto

```
agendas-api/
├── core/                # Configurações do projeto Django
│   ├── settings.py      # Configurações gerais
│   ├── urls.py          # URLs globais
│   └── wsgi.py          # Configuração WSGI
├── agenda/              # Aplicativo de agendas
│   ├── models.py        # Modelos de dados
│   ├── serializers.py   # Serializadores para API REST
│   ├── views.py         # Visualizações da API
│   ├── urls.py          # Rotas da API
│   └── tests.py         # Testes unitários
├── Dockerfile           # Configuração do Docker
├── docker-compose.yml   # Configuração do Docker Compose
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

## Testes

Para executar os testes:

```bash
python manage.py test
```

## Conclusão

Este plano de desenvolvimento utilizando Django oferece uma solução robusta e escalável para o desafio proposto. O Django REST Framework facilita a criação de APIs RESTful, enquanto o Swagger fornece documentação automática. A conteinerização com Docker simplifica a implantação e reprodução do ambiente de desenvolvimento.

O projeto atende a todos os requisitos obrigatórios:

* API RESTful para CRUD de agendas
* Máquina de estados para agendas
* Conteinerização com Docker
* Documentação detalhada
* (Opcional) Front-end em React
