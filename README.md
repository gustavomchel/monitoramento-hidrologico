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
venv\Scripts\activate
```

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 1.3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 2. Preparar o banco de dados

```bash
python manage.py migrate
```

### 2.1. Gerar e importar os dados

```bash
python seed.py
python import_csv.py
```

O `seed.py` gera os dados sintéticos em CSV, enquanto o `import_csv.py` importa os registros para o banco SQLite.

## 3. Executar a aplicação

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

`http://127.0.0.1:8000/`
