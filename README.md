# Monitoramento Hidrológico

API REST desenvolvida com Django e Django REST Framework para consultar dados sintéticos de monitoramento de nível de rios e intensidade de chuva.

> **Aviso:** os dados são fictícios e possuem finalidade exclusivamente demonstrativa.

## 0. Requisitos Funcionais

## 0. Regras de negócio

## 1. Tecnologias

- Python
- Django
- Django REST Framework
- SQLite
- DRF Spectacular
- CSV

## 2. Modelo relacional

O banco de dados possui duas entidades relacionadas:

**Station (Estação)**

| Campo | Descrição |
|---|---|
| `id` | Identificador da estação (PK) |
| `name` | Nome da estação |
| `river` | Rio monitorado |
| `municipality` | Município |

**Observation (Observação)**

| Campo | Descrição |
|---|---|
| `id` | Identificador da observação (PK) |
| `station_id` | Estação relacionada (FK) |
| `observed_at` | Data e hora da observação |
| `value` | Valor observado |
| `metric` | Métrica monitorada |
| `unit` | Unidade de medida |
| `source` | Origem dos dados |

**Relacionamento: 1:N**

Uma estação pode possuir várias observações, mas cada observação pertence a uma única estação.

## 3. Regras e decisões técnicas

- **Métricas:** `level` (nível do rio) e `rain` (intensidade de chuva).
- **Unidades:** metros (`m`) para nível e milímetros por hora (`mm/h`) para chuva.
- **Origem:** registros identificados como `synthetic`.
- **Integridade:** restrições para evitar duplicidades e garantir a correspondência entre métrica e unidade.
- **Índice:** composto por estação, métrica e horário para otimizar consultas históricas.
- **Período:** consultas de 1 a 72 horas, com padrão de 24 horas.
- **Horários:** armazenados e apresentados em UTC.
- **Séries históricas:** ordenadas cronologicamente. Períodos sem registros permanecem sem preenchimento artificial.

## 4. Arquitetura

A aplicação separa as responsabilidades entre os seguintes módulos:

| Diretório ou arquivo | Responsabilidade |
|---|---|
| `setup/` | Pacote de configuração principal do projeto Django |
| `setup/settings.py` | Configurações gerais, aplicativos, banco de dados e middlewares |
| `setup/urls.py` | Define o roteamento global aplicação |
| `setup/__init__.py` | Identifica o diretório como um pacote python |
| `docs` | Modelagem dos dados |
| `scripts/` | Gera os dados e envia para os arquivos csv |
| `data/` | Arquivos com os dados gerados pelo script seed.py |
| `monitoring/management/commands/import_csv.py` | Importa os dados e por meio dos modelos orm, envia para o banco de dados SQLite |
| `monitoring/migrations` |
| `monitoring/static/` |
| `monitoring/templates/` | Templates HTML |
| `monitoring/__init__.py` |
| `monitoring/admin.py` |
| `monitoring/apps.py` |
| `monitoring/models.py` | Modelos e regras de integridade |
| `monitoring/tests.py` |
| `monitoring/urls.py` |
| `monitoring/views.py` |
| `api/apps.py` | Configura o aplicativo 'api' no Django |
| `api/serializers.py` | Define a conversão dos modelos em dados JSON |
| `api/tests.py` |
| `api/urls.py` | Registra as rotas e associa as requisições às respectivas views |
| `api/views.py` | Processamento das requisições |
| `.env` | Armazena a chave secreta do Django, o modo de depuração e os hosts permitidos |
| `.gitignore` | Define arquivos ignorados pelo Git |
| `db.sqlite3` | Banco de dados SQLite |
| `manage.py` | Gerenciamento do Django |
| `README.md` | Manual de instruções |

### Funcionamento do roteamento

O roteamento utiliza o `DefaultRouter` para registrar automaticamente as rotas do `StationViewSet`.

- `setup/urls.py`: define o prefixo `/api/` e encaminha as requisições para `api.urls`.
- `api/urls.py`: registra o `StationViewSet` com o prefixo `stations`.
- `api/views.py`: implementa as operações e ações personalizadas.

O `ModelViewSet` disponibiliza operações padrão, como listagem e consulta individual. O decorador `@action` registra ações adicionais, como `summary` e `series`.

## 5. Endpoints disponíveis

| Método | Endpoint | Finalidade |
|---|---|---|
| GET | `/api/stations` | Lista as estações disponíveis |
| GET | `/api/stations/{id}/summary` | Retorna os dados da estação e suas últimas leituras |
| GET | `/api/stations/{id}/series?metric=level&hours=24` | Consulta o histórico de nível do rio em metros |
| GET | `/api/stations/{id}/series?metric=rain&hours=24` | Consulta o histórico de chuva em mm/h |

### Parâmetros de consulta

| Parâmetro | Valores | Padrão |
|---|---|---|
| `metric` | `level` ou `rain` | Obrigatório |
| `hours` | Inteiro entre 1 e 72 | 24 |

As duas consultas históricas utilizam a mesma rota `series`. A métrica informada determina quais observações serão recuperadas.

## 6. Como executar

### Pré-requisitos

- Python instalado.
- Git instalado.

### 6.1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
```

### 6.2. Criar e ativar o ambiente virtual

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 6.3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6.4. Preparar o banco de dados

```bash
python manage.py migrate
```

### 6.5. Gerar e importar os dados

```bash
python seed.py
python import_csv.py
```

O `seed.py` gera os dados sintéticos em CSV, enquanto o `import_csv.py` importa os registros para o banco SQLite.

A importação deve permite execuções repetidas sem duplicar registros.

### 6.6. Executar a aplicação

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

`http://127.0.0.1:8000/`

## 7. Documentação e testes

A documentação da API foi gerada com DRF Spectacular.

| Recurso | Endereço | Descrição |
|---|---|
| Swagger UI | `/api/docs/` | Interface interativa para testar a API. |
| ReDoc | `/api/redoc/` | Documentação visual dos endpoints. |
| Esquema OpenAPI | `/api/schema/` | Estrutura da documentação da API. |
| Django Admin | `/admin/` | Interface administrativa do Django. |

As requisições são testadas pela Browsable API do Django REST Framework.

Exemplos:

```text
GET http://127.0.0.1:8000/api/stations

GET http://127.0.0.1:8000/api/stations/EST-01/summary

GET http://127.0.0.1:8000/api/stations/EST-01/series?metric=level&hours=24

GET http://127.0.0.1:8000/api/stations/EST-01/series?metric=rain&hours=24
```

## 8. Tratamento de erros

A API prevê:

- HTTP 400: parâmetros inválidos ou período fora do intervalo permitido.
- HTTP 404: estação não encontrada.
- HTTP 200 com `points` vazio: nenhuma observação encontrada no período solicitado.

A ausência de observações não é interpretada como falha nem resulta na criação de dados artificiais.

## Contribuições da equipe

| Integrante | Contribuições |
|---|---|
| Gustavo Michel Luna Ribeiro | Elaboração do README, implementação dos Models, desenvolvimento do processo de geração de dados sintéticos e importação para o banco de dados. |
| Renato Moreira | Elaboração da modelagem do projeto, implementação dos endpoints de consulta de séries históricas, filtros e autenticação da API, além da configuração da documentação com DRF Spectacular. |
| Vitor Hugo da Silva Araújo | Configuração do ambiente de desenvolvimento, gerenciamento do Trello e do repositório no GitHub, implementação do template da interface e do endpoint de consulta de resumos das estações. |

---

**Monitoramento Hidrológico:** projeto demonstrativo de modelagem relacional, desenvolvimento de API REST, consultas históricas e documentação com Django REST Framework.