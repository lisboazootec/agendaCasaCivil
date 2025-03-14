FROM python:3.11-slim

# Configurar ambiente para desenvolvimento
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt



# Criar diretório para o banco de dados
RUN mkdir -p /app/data && chmod 777 /app/data

# Expor a porta
EXPOSE 8000

