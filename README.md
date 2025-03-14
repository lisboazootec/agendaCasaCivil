# 🗓️ Agendas - Sistema de Gerenciamento de Agendas

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-red?style=for-the-badge&logo=djanog&logoColor=white)](https://www.django-rest-framework.org/)
[![Nuxt.js](https://img.shields.io/badge/Nuxt.js-00C58E?style=for-the-badge&logo=nuxt.js&logoColor=white)](https://nuxt.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)](https://vuejs.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Shadcn/ui](https://img.shields.io/badge/Shadcn%2Fui-black?style=for-the-badge&logo=shadcn%2Fui&logoColor=white)](https://ui.shadcn.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![Faker](https://img.shields.io/badge/Faker-B348BB?style=for-the-badge&logo=faker&logoColor=white)](https://faker.readthedocs.io/en/master/)
[![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?style=for-the-badge&logo=pre-commit&logoColor=white)](https://pre-commit.com/)

> Um sistema full-stack moderno e eficiente para gerenciamento de agendas, construído com as melhores tecnologias do mercado!

Este projeto foi desenvolvido como parte do desafio técnico proposto pela **Presidência da República (Secretaria-Executiva da Casa Civil / SSGINF / CGSE)** para o processo seletivo.

## ✨ Funcionalidades Principais

Este sistema oferece um conjunto completo de recursos para gerenciar agendas de forma eficaz:

* **Backend (API RESTful):**

  * **CRUD Completo:** Crie, leia, atualize e exclua agendas com facilidade.  Cada operação é cuidadosamente implementada para garantir a integridade dos dados.
  * **Máquina de Estados:** Gerencie o ciclo de vida de cada agenda através de uma máquina de estados bem definida.  Os estados possíveis são:
    * `RECEBIDO`: A agenda foi criada, mas ainda não foi confirmada.
    * `CONFIRMADO`: A agenda foi confirmada e está agendada.
    * `ATENDIDO`: A agenda foi cumprida.
    * `CANCELADO`: A agenda foi cancelada.
    * A transição entre os estados é controlada de forma lógica e consistente.
  * **Paginação:**  Listagem de agendas otimizada com paginação, permitindo lidar com um grande volume de dados sem comprometer o desempenho.
  * **Documentação Automática (Swagger/ReDoc):**  A API é totalmente documentada com Swagger e ReDoc, facilitando a integração e o entendimento dos endpoints.  Você pode explorar e testar a API diretamente do seu navegador!
  * **Testes Unitários:**  Cobertura abrangente de testes unitários para garantir a qualidade, confiabilidade e robustez do código.
  * **População de Dados (Faker):**  Um script (`populate_agenda.py`) está incluído para popular rapidamente o banco de dados com dados de teste realistas, usando a biblioteca Faker.  Isso facilita a experimentação e o desenvolvimento.
* **Frontend (Interface Web):**

  * **Interface Moderna e Intuitiva:**  Uma interface de usuário amigável, responsiva e visualmente agradável, construída com as tecnologias mais modernas:
    * **Nuxt 3:**  Framework Vue.js poderoso, com Server-Side Rendering (SSR) para melhor performance e SEO.
    * **Vue 3:**  Framework JavaScript progressivo para construir interfaces interativas e reativas.
    * **Tailwind CSS:**  Framework CSS utilitário para estilização rápida, consistente e responsiva.
    * **Shadcn/ui:**  Biblioteca de componentes UI acessíveis, customizáveis e de alta qualidade, agilizando o desenvolvimento e garantindo uma ótima experiência do usuário.
  * **Funcionalidades:**
    * **Listagem de Agendas:** Visualize todas as agendas em uma lista clara, com paginação para facilitar a navegação.
    * **Criação de Agendas:**  Adicione novas agendas através de um formulário intuitivo.
    * **Edição de Agendas:**  Edite todos os campos de uma agenda existente.
    * **Exclusão de Agendas:**  Exclua agendas com segurança, com uma etapa de confirmação para evitar exclusões acidentais.
    * **Alteração de Estado:**  Altere o estado de uma agenda (Recebido, Confirmado, Atendido, Cancelado) de forma simples e direta.
    * **Calendário Interativo:** Visualize e crie novos agendamentos em um calendário.
* **Infraestrutura (Docker):**

  * **Conteinerização Completa:**  A aplicação é totalmente conteinerizada com Docker e Docker Compose, o que significa que você pode executá-la em *qualquer* ambiente que suporte Docker, com *apenas um comando*!  Isso elimina problemas de dependências e configurações, garantindo que a aplicação funcione da mesma forma em qualquer lugar.
  * **Implantação Simplificada:**  A conteinerização torna a implantação em ambientes de produção (como servidores cloud) extremamente fácil e rápida.

## 📁 Estrutura Detalhada do Projeto

```

.
├── agendas-api/          # Backend (Django) - Coração da aplicação!
│   ├── agenda/           # App Django principal - Onde a mágica acontece!
│   │   ├── admin.py      # Configuração do admin Django (interface administrativa)
│   │   ├── apps.py       # Configuração do app
│   │   ├── management/   # Comandos customizados (ex: populate_agenda)
│   │   │   └── commands/
│   │   │       └── populate_agenda.py  # Script para popular o BD com dados falsos (Faker)
│   │   ├── migrations/   # Migrações do banco de dados (evolução do schema)
│   │   ├── models.py     # Modelos de dados (a classe Agenda) - Define a estrutura dos dados
│   │   ├── serializers.py# Serializadores para a API REST - Converte dados do Python para JSON e vice-versa
│   │   ├── tests.py      # Testes unitários - Garantem a qualidade do código!
│   │   ├── urls.py       # URLs do app - Mapeia as URLs para as views
│   │   └── views.py      # Views da API (a lógica!) - Processa as requisições e retorna as respostas
│   ├── core/             # Projeto Django (configurações) - Configurações globais do projeto
│   │   ├── settings.py   # Configurações do Django (banco de dados, segurança, etc.)
│   │   ├── urls.py       # URLs do projeto - Mapeia as URLs para os apps
│   │   └── ...
│   ├── db.sqlite3        # Banco de dados SQLite (gerenciado pelo Docker, ótimo para desenvolvimento)
│   ├── Dockerfile        # Dockerfile para o backend - Receita para criar a imagem Docker do backend
│   ├── manage.py         # Script de gerenciamento do Django (para rodar comandos como migrate, runserver, etc.)
│   └── requirements.txt  # Dependências do Python (backend) - Lista de bibliotecas necessárias
│
├── agendas-frontend/     # Frontend (Nuxt 3) - A interface com o usuário!
│   ├── app.vue            # Componente principal do Nuxt
│   ├── assets/           # Arquivos estáticos (CSS, imagens, etc.)
│   ├── components/       # Componentes Vue - Blocos de construção da interface
│   │   └── ui/            # Componentes Shadcn/ui - Componentes prontos e estilosos!
│   ├── composables/      # Composables (lógica reutilizável)
│   │   └── useApi.ts      # Composable para interagir com a API do backend
│   ├── nuxt.config.ts    # Configuração do Nuxt
│   ├── pages/            # Páginas do aplicativo (rotas) - As diferentes telas da aplicação
│   │   ├── index.vue      # Página principal (listagem de agendas)
│   │   ├── create.vue     # Página de criação de agenda
│   │   └── edit/[id].vue  # Página de edição de agenda
│   ├── Dockerfile        # Dockerfile para o frontend - Receita para criar a imagem Docker do frontend
│   ├── package.json      # Dependências do Node.js (frontend) - Lista de bibliotecas necessárias
│   └── ...
│
├── docker-compose.yml   # Configuração do Docker Compose - Orquestra o backend, frontend e banco de dados!
└── README.md             # Este arquivo - O guia completo do projeto!

```

## 🚀 Tecnologias Utilizadas: Um Arsenal Completo!

Este projeto foi construído com um conjunto de tecnologias modernas e robustas, escolhidas a dedo para garantir a melhor performance, escalabilidade e manutenibilidade:

* **Backend:**

  * ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) **Python 3.11:** A linguagem de programação principal, conhecida por sua sintaxe clara e versatilidade.
  * ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=green) **Django 4.2:** Um framework web de alto nível, que incentiva o desenvolvimento rápido e limpo, seguindo o princípio DRY (Don't Repeat Yourself).
  * ![DRF](https://img.shields.io/badge/DRF-red?style=flat-square&logo=django&logoColor=white) **Django REST Framework (DRF):** Uma ferramenta poderosa e flexível para construir APIs RESTful, com recursos como serialização, autenticação e validação.
  * ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white) **SQLite:** Um banco de dados leve e fácil de usar, perfeito para desenvolvimento e prototipagem. (Em produção, recomenda-se um banco de dados mais robusto, como PostgreSQL).
  * ![Faker](https://img.shields.io/badge/Faker-B348BB?style=flat-square&logo=faker&logoColor=white) **Faker:** Uma biblioteca Python que gera dados falsos, mas realistas (nomes, endereços, datas, etc.), ideal para popular o banco de dados para testes.
  * **drf-yasg:** Gera automaticamente a documentação da API nos formatos Swagger e ReDoc, tornando a API fácil de entender e usar.
  * **pre-commit:**  Garante a qualidade do código executando linters e formatadores automaticamente antes de cada commit.
  * **gunicorn:** Servidor HTTP WSGI para executar aplicações Django em produção.
* **Frontend:**

  * ![Nuxt.js](https://img.shields.io/badge/Nuxt.js-00C58E?style=flat-square&logo=nuxtdotjs&logoColor=white) **Nuxt 3:** Um framework Vue.js que oferece recursos como Server-Side Rendering (SSR), roteamento automático e otimizações de performance, tornando a aplicação rápida e amigável para os motores de busca.
  * ![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white) **Vue 3:** Um framework JavaScript progressivo para construir interfaces de usuário interativas e reativas, com uma sintaxe simples e elegante.
  * ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white) **Tailwind CSS:** Um framework CSS utilitário que permite estilizar a aplicação rapidamente, usando classes pré-definidas para criar layouts responsivos e personalizados.
  * ![Shadcn/ui](https://img.shields.io/badge/Shadcn%2Fui-black?style=flat-square&logo=shadcnui&logoColor=white) **Shadcn/ui:** Uma coleção de componentes UI reutilizáveis, construídos com Tailwind CSS, que aceleram o desenvolvimento e garantem um visual moderno e consistente.
  * **date-fns:** Uma biblioteca JavaScript para manipular datas e horas de forma fácil e eficiente.
  * **axios:** (Já incluso no Nuxt) Um cliente HTTP para fazer requisições à API do backend de forma simples e assíncrona.
* **Infraestrutura:**

  * ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) **Docker:** Uma plataforma para conteinerizar aplicações, empacotando o código e suas dependências em um "container" isolado, garantindo que a aplicação funcione da mesma forma em qualquer ambiente.
  * **Docker Compose:** Uma ferramenta para definir e gerenciar aplicações multi-container, facilitando a orquestração do backend, frontend e banco de dados.

## ⚙️ Pré-requisitos: O Que Você Precisa

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

* ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) [Docker](https://www.docker.com/get-started):  O Docker é essencial para executar a aplicação de forma conteinerizada.
* [Docker Compose](https://docs.docker.com/compose/install/): O Docker Compose facilita a execução e o gerenciamento dos múltiplos containers da aplicação.

## 🚀 Execução com Docker: A Forma Mais Fácil!

A maneira mais simples e rápida de executar o projeto é usando o Docker Compose.  Com *um único comando*, você terá tudo funcionando!

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/lisboazootec/agendaCasaCivil
   cd agendaCasaCivil
   ```

   Substitua `<URL_DO_SEU_REPOSITORIO>` pela URL do seu repositório Git e `<NOME_DA_PASTA_DO_PROJETO>` pelo nome da pasta onde o projeto foi clonado.
2. **Construa e Inicie os Containers:**

   ```bash
   docker-compose up --build
   ```

   * Use `--build` quando quiser garantir que todas as alterações nos arquivos de build sejam aplicadas
   * Use `-d` quando quiser que os contêineres rodem em segundo plano, sem ocupar seu terminal
   * **`docker-compose up`:**  Inicia os serviços definidos no arquivo `docker-compose.yml` (backend, frontend, banco de dados e um serviço especial para abrir o navegador).
   * **`--build`:**  Constrói as imagens Docker do backend e do frontend *antes* de iniciar os containers.  Use este argumento sempre que você modificar o código ou as dependências (arquivos `Dockerfile`, `requirements.txt` ou `package.json`).
   * O Docker Compose se encarregará de baixar as imagens base (Python, Node.js), instalar as dependências, executar as migrações do Django, popular o banco de dados e iniciar os servidores.  Tudo de forma automática!
3. **Aguarde a Inicialização:**

   O processo de build e inicialização pode levar alguns minutos, especialmente na primeira vez.  Você verá mensagens no terminal indicando o progresso.  O serviço `openbrowser` abrirá automaticamente as seguintes URLs no seu navegador padrão:

   * **Frontend:** `http://localhost:3000`
   * **Backend (API):** `http://localhost:8000/api/`
   * **Documentação da API (Swagger):** `http://localhost:8000/swagger/`
   * **Documentação da API (ReDoc):** `http://localhost:8000/redoc/`

   Se, por algum motivo, os navegadores não abrirem automaticamente, você pode acessá-los manualmente.
   Pronto!  A aplicação estará rodando e você poderá começar a usá-la e explorá-la.

## 💻 Execução Local (Sem Docker): Para Desenvolvedores

Se você preferir executar o projeto *diretamente* na sua máquina (sem Docker), siga estes passos.  Isso é útil para desenvolvimento mais avançado, depuração e personalização.

**Backend (Django):**

1. **Pré-requisitos (Backend):**

   * Python 3.11+ instalado.
   * `pip` (gerenciador de pacotes do Python) instalado.
   * Um ambiente virtual (altamente recomendado!).
2. **Clone o Repositório:**

   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd <NOME_DA_PASTA_DO_PROJETO>/agendas-api
   ```
3. **Crie e Ative um Ambiente Virtual:**

   ```bash
   python3 -m venv venv  # Cria o ambiente virtual (pasta 'venv')
   source venv/bin/activate  # Ativa o ambiente virtual (Linux/macOS)
   # venv\Scripts\activate  # Ativa o ambiente virtual (Windows)
   ```

   Usar um ambiente virtual é *altamente recomendado* para isolar as dependências do projeto e evitar conflitos com outras bibliotecas instaladas no seu sistema.
4. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```
5. **Execute as Migrações:**

   ```bash
   python manage.py migrate
   ```

   Este comando aplica as migrações do Django, criando as tabelas necessárias no banco de dados SQLite.
6. **Popule o Banco de Dados (Opcional):**
   no modo  de containers  já executa esse comando

   ```bash
   python manage.py populate_agenda
   ```

   Este comando executa o script `populate_agenda.py`, que usa a biblioteca Faker para criar dados de teste realistas e preencher o banco de dados.  Isso é útil para testar a aplicação.
   Ex: 2

   ```bash
   python manage.py populate_agenda 50 // Inserir 50 tuplas de dados 
   ```
9. **Inicie o Servidor de Desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   Este comando inicia o servidor de desenvolvimento do Django.  O backend estará acessível em `http://localhost:8000`.

**Frontend (Nuxt 3):**

1. **Pré-requisitos (Frontend):**

   * Node.js (versão 18 ou superior) e npm instalados.
2. **Navegue até a Pasta do Frontend:**

   ```bash
   cd ../agendas-frontend
   ```
3. **Instale as Dependências:**

   ```bash
   npm install --legacy-peer-deps
   ```

   O `--legacy-peer-deps` pode ser necessário em alguns casos para resolver conflitos de dependências.
4. **Inicie o Servidor de Desenvolvimento:**

   ```bash
   npm run dev
   ```

   Este comando inicia o servidor de desenvolvimento do Nuxt.  O frontend estará acessível em `http://localhost:3000`.
5. **Configure o Arquivo `.env` (Importante!):**

   * Crie um arquivo chamado `.env` na pasta `agendas-frontend`.
   * Adicione a seguinte linha ao arquivo `.env`:

     ```
     NUXT_PUBLIC_API_BASE=http://localhost:8000/api
     ```

     Esta variável de ambiente informa ao frontend onde encontrar a API do backend.

## 🧪 Testes: Garantindo a Qualidade

Para executar os testes unitários do backend (Django), use o seguinte comando:

```bash
# Com Docker:
docker-compose exec backend python manage.py test

# Sem Docker:
cd agendas-api
source venv/bin/activate  # Ative o ambiente virtual (se estiver usando)
python manage.py test
```

Os testes unitários verificam se as diferentes partes do backend (models, serializers, views) estão funcionando corretamente.  É uma boa prática executar os testes sempre que você fizer alterações no código.

## 🌐 Endpoints da API (Backend): Explorando a API RESTful

A API RESTful do backend oferece os seguintes endpoints para interagir com as agendas:

* **`GET /api/agendas/`:**

  * **Descrição:** Retorna uma lista *paginada* de todas as agendas.
  * **Exemplo de Resposta:**

    ```json
    {
        "count": 12,  // Número total de agendas
        "next": "http://localhost:8000/api/agendas/?page=2",  // URL da próxima página (se houver)
        "previous": null,  // URL da página anterior (se houver)
        "results": [  // Lista de agendas (resultados da página atual)
            {
                "id": 1,
                "titulo": "Reunião de Projeto",
                "descricao": "Discussão sobre o andamento do projeto.",
                "dataInicio": "2024-07-27T10:00:00Z",
                "dataFim": "2024-07-27T11:30:00Z",
                "local": "Sala de Reuniões 1",
                "estadoAtualAgenda": "CONFIRMADO"
            },
            {
                "id": 2,
                "titulo": "Consulta Médica",
                "descricao": "Check-up de rotina.",
                "dataInicio": "2024-07-28T14:00:00Z",
                "dataFim": "2024-07-28T14:45:00Z",
                "local": "Clínica Bem-Estar",
                "estadoAtualAgenda": "RECEBIDO"
            },
            ...  // Outras agendas
        ]
    }
    ```
* **`POST /api/agendas/`:**

  * **Descrição:** Cria uma nova agenda.
  * **Corpo da Requisição (JSON):**

    ```json
    {
      "titulo": "Reunião de Planejamento",
      "descricao": "Discussão sobre os próximos projetos",
      "dataInicio": "2024-07-27T14:00:00-03:00",  // Formato ISO 8601 com timezone offset
      "dataFim": "2024-07-27T16:00:00-03:00",    // Formato ISO 8601 com timezone offset
      "local": "Sala de Reuniões 2",
      "estadoAtualAgenda": "RECEBIDO"  // Estado inicial da agenda
    }
    ```

    **Importante:**  As datas (`dataInicio` e `dataFim`) *devem* ser enviadas em formato ISO 8601 *com* o timezone offset (ex: `-03:00` para o horário de Brasília).  Isso garante que as datas sejam interpretadas corretamente, independentemente do fuso horário do servidor ou do cliente.
  * **Resposta (201 Created):** Retorna a agenda criada, incluindo o `id` gerado automaticamente.
* **`GET /api/agendas/<id>/`:**

  * **Descrição:** Retorna os detalhes de uma agenda específica, identificada pelo `id`.
* **`PUT /api/agendas/<id>/`:**

  * **Descrição:** Atualiza *todos* os campos de uma agenda.  Você *deve* enviar *todos* os campos, mesmo que eles não tenham sido alterados.  Se você omitir um campo, ele será definido como `null` (ou o valor padrão do campo).
* **`PATCH /api/agendas/<id>/`:**

  * **Descrição:** Atualiza *parcialmente* uma agenda.  Você só precisa enviar os campos que deseja modificar.  Os campos omitidos permanecerão inalterados.
* **`DELETE /api/agendas/<id>/`:**

  * **Descrição:** Exclui uma agenda, identificada pelo `id`.
* **`PATCH /api/agendas/<id>/estado/`:**

  * **Descrição:** *Endpoint especial* para alterar o *estado* de uma agenda.  Isso simplifica a atualização do estado sem precisar enviar todos os outros campos.
  * **Corpo da Requisição (JSON):**

    ```json
    {
      "estadoAtualAgenda": "CONFIRMADO"  // Novo estado da agenda
    }
    ```
  * **Valores Válidos para `estadoAtualAgenda`:**  `RECEBIDO`, `CONFIRMADO`, `ATENDIDO`, `CANCELADO`.

## 📄 Documentação da API (Swagger/ReDoc): Explore e Teste!

A API é *automaticamente* documentada usando `drf-yasg`, que gera documentação interativa nos formatos Swagger e ReDoc.  Isso é *extremamente* útil para:

* **Explorar os Endpoints:**  Veja todos os endpoints disponíveis, seus parâmetros, formatos de requisição e resposta.
* **Entender a API:**  A documentação fornece descrições claras de cada endpoint e seus campos.
* **Testar a API:**  Você pode *testar* a API diretamente do seu navegador, enviando requisições e vendo as respostas em tempo real!

Acesse a documentação nos seguintes endereços:

* [Swagger UI (Interface interativa)](http://localhost:8000/swagger/)
* [ReDoc (Interface mais limpa e focada)](http://localhost:8000/redoc/)

## 📝 Backlog (Exemplo): Ideias para o Futuro!

Este é um exemplo de backlog, com algumas ideias para expandir e aprimorar o projeto:

1. **Backend:**

   * [X] Configurar projeto Django e Django REST Framework.
   * [X] Criar modelo `Agenda` com os campos especificados.
   * [X] Implementar serializers para o modelo `Agenda`.
   * [X] Implementar views (API endpoints) para CRUD de agendas.
   * [X] Implementar view para alteração de estado da agenda.
   * [X] Configurar paginação para a listagem de agendas.
   * [X] Adicionar documentação da API com Swagger/ReDoc.
   * [X] Escrever testes unitários para os endpoints da API.
   * [X] Criar script para popular o banco de dados com dados de teste.
   * [X] Dockerizar o backend.
   * [ ] **Adicionar Autenticação e Autorização:**  Implementar um sistema de autenticação e autorização para proteger a API e garantir que apenas usuários autorizados possam acessar e modificar os dados.  Você pode usar bibliotecas como `djangorestframework-simplejwt` ou `djoser`.
   * [ ] **Adicionar Filtros para a Listagem de Agendas:**  Permitir que os usuários filtrem as agendas por data, estado, local, etc., usando parâmetros na URL (ex: `/api/agendas/?dataInicio=2024-08-01&estadoAtualAgenda=CONFIRMADO`).  Você pode usar a biblioteca `django-filter` para facilitar a implementação.
   * [ ] **Adicionar Busca:** Implemente um endpoint de busca para procurar agendas por título, descrição ou outros campos.
   * [ ] **Adicionar Upload de Anexos** Adicione a opção de fazer upload de arquivos, integrando-os às agendas por meio de um relacionamento na base de dados, proporcionando uma maneira conveniente de incluir documentos, imagens ou outros arquivos relevantes nos agendamentos.
   * [ ] **Logs:** Adicionar logs detalhados para rastrear as ações realizadas na aplicação, facilitando a depuração e o monitoramento.
   * [ ] **Validação Personalizada:**  Adicionar validação personalizada aos serializers para garantir regras de negócio mais complexas (ex: verificar se não há conflitos de horário entre agendas).
   * [ ] **Usar um Banco de Dados Robusto em Produção:**  Substituir o SQLite por um banco de dados mais adequado para produção, como PostgreSQL ou MySQL.
   * [ ] **Testes de Integração:**  Adicionar testes de integração para verificar a interação entre diferentes partes da aplicação (ex: testar se o frontend consegue se comunicar corretamente com o backend).
2. **Frontend:**

   * [X] Configurar projeto Nuxt 3.
   * [X] Criar layout básico da aplicação.
   * [X] Criar componente para listar agendas.
   * [X] Criar componente para exibir detalhes de uma agenda.
   * [X] Criar componente/formulário para criar uma nova agenda.
   * [X] Criar componente/formulário para editar uma agenda existente.
   * [X] Implementar a exclusão de agendas (com confirmação).
   * [X] Implementar a alteração de estado da agenda.
   * [X] Adicionar paginação à listagem de agendas.
   * [X] Adicionar tratamento de erros (ex: exibir mensagens de erro da API).
   * [X] Dockerizar o frontend.
   * [X] Adicionar calendário.
   * [ ] **Adicionar Testes Unitários para os Componentes:**  Escrever testes unitários para os componentes Vue, usando bibliotecas como Vue Test Utils ou Jest.
   * [ ] **Melhorar a Estilização e Responsividade:**  Refinar a estilização da aplicação, garantindo que ela seja totalmente responsiva e visualmente atraente em diferentes tamanhos de tela.
   * [ ] **Adicionar Funcionalidades de Busca e Filtro:**  Integrar a busca e os filtros implementados no backend ao frontend, permitindo que os usuários pesquisem e filtrem as agendas de forma interativa.
   * [ ] **Adicionar Notificações:**  Implementar notificações (ex: notificações push, e-mail) para lembrar os usuários sobre suas agendas.
   * [ ] **Adicionar Loading Skeletons/Spinners**: Exibir indicadores de carregamento (skeletons ou spinners) enquanto os dados estão sendo buscados da API, melhorando a experiência do usuário.
   * [ ] **Adicionar um componente para lidar com a visualização e upload dos arquivos** Adicionar a capacidade de visualizar e fazer upload de arquivos no frontend, conectando-o ao backend para armazenamento e recuperação.
   * [ ] **Internacionalização (i18n):**  Tornar a aplicação multi-idioma, usando bibliotecas como `vue-i18n` ou `nuxt-i18n`.
   * [ ] **Implementar PWA**: Transformar o frontend em um Progressive Web App (PWA) para oferecer uma experiência mais nativa, com funcionalidades offline e notificações push.
   * [ ] **Dark Mode**: Implementar um tema escuro para a aplicação, melhorando a acessibilidade e a experiência do usuário em ambientes com pouca luz.
   * [ ] **Acessibilidade (a11y):**  Garantir que a aplicação seja acessível para pessoas com deficiência, seguindo as diretrizes WCAG.
3. **Integração:**

   * [X] Criar arquivo `docker-compose.yml` para orquestrar backend e frontend.
   * [X] Configurar o frontend para consumir a API do backend.
   * [X] Configurar variáveis de ambiente para URLs da API, etc.
4. **Documentação:**

   * [X] Escrever README.md detalhado com instruções de configuração e uso (este documento!).
   * [ ] **Documentar o Código (Docstrings):**  Adicionar docstrings (comentários em formato específico) a todas as funções, classes e métodos do backend, para gerar documentação do código automaticamente.

## 🤝
