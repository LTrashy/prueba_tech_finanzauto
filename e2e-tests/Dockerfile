# e2e-tests/Dockerfile
FROM mcr.microsoft.com/playwright:focal

WORKDIR /workspace

# Copiar el código (tests incluidos)
COPY . .

# Crear package.json si no existe e instalar @playwright/test
RUN test -f package.json || npm init -y && \
    npm install @playwright/test@latest && \
    npx playwright install --with-deps

CMD ["npx", "playwright", "test", "--reporter=list"]
