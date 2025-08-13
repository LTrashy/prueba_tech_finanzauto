# api-tests/Dockerfile
FROM python:3.10-slim

# Evitar prompts y configurar entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema (curl opcional para debug)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de tests
COPY . .

# Comando por defecto: ejecutar pytest
CMD ["pytest", "-q", "--maxfail=1", "--disable-warnings"]
