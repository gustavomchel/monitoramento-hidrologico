# Monitoramento Hidrológico

API REST desenvolvida com Django e Django REST Framework para consultar dados sintéticos de monitoramento de nível de rios e intensidade de chuva.

> **Aviso:** os dados são fictícios e possuem finalidade exclusivamente demonstrativa.


## 1. Criação de ambiente

### Pré-requisitos

- Python instalado.
- Git instalado.

### 1.1. Clonar o repositório

```bash
git clone https://github.com/vitorhngo/monitoramento-hidrologico.git
cd monitoramento-hidrologico
```

### 1.2. Criar e ativar o ambiente virtual

Windows:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 1.3. Instalar as dependências

Antes de executar comandos ou rodar o projeto, certifique-se de que o Python do ambiente virtual (venv) esteja ativo.

1. Pressione Ctrl + Shift + P para abrir a paleta de comandos.
2. Digite e selecione Python: Select Interpreter.
3. Escolha a opção que contém o caminho da pasta da sua venv (ex: .\venv\Scripts\python.exe).

```bash
python -m pip install -r requirements.txt
```

> **Aviso:** O início `python -m pip` garante que o pip seja vinculado exatamente ao Python da sua venv atual, evitando instalações acidentais no sistema global e conflitos futuros de sistema. 

### 1.4. Criar variáveis de ambiente
1. Copie o arquivo `.env.example`, colocando-o na raiz do projeto.
2. Renomeie-o para `.env`
3. No terminal, rode o comando abaixo:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
4. Copie o código que aparece. No arquivo `.env`, substitua *replace-with-your-own-secret-key* pelo código copiado.

## 2. Preparar o banco de dados

```bash
python manage.py migrate
```

### 2.1. Gerar e importar os dados

```bash
python scripts/seed.py
python manage.py import_csv
```

O `seed.py` gera os dados sintéticos em CSV, enquanto o `import_csv` importa os registros para o banco SQLite.

## 3. Executar a aplicação

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

`http://127.0.0.1:8000/`
