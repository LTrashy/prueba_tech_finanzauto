# 🧪 Proyecto de Automatización de Pruebas

Este proyecto contiene tres tipos de pruebas automatizadas:
1. **Pruebas API** con Pytest
2. **Pruebas End-to-End (E2E)** con Selenium + Chrome (noVNC)
3. **Pruebas de Performance** con Locust

Todo se ejecuta en contenedores Docker usando `docker-compose up --build`.

---

## 📋 1. Pruebas API
Ubicación: `./api-tests`

### Descripción
Pruebas automatizadas sobre endpoints de API, verificando:
- Respuestas HTTP correctas
- Validación de esquemas JSON
- Casos positivos y negativos

### Cómo ejecutar
```bash
docker compose up api-tests
```
---

### 📋 2. Pruebas End-to-End (E2E)
Ubicación: `./e2e-tests`

### Descripción

Automatización sobre la web The Internet - Herokuapp incluyendo:
- Formularios complejos (/checkboxes, /dropdown, /dynamic_controls)
- Autenticación (/login)
- Elementos dinámicos (/dynamic_loading)
- Subida/Bajada de archivos (/upload, /download)
- Drag & Drop (/drag_and_drop)
- Hovers y tooltips (/hovers)
- JavaScript alerts (/javascript_alerts)
- Múltiples ventanas (/windows)

### Cómo ejecutar
```bash
docker compose up e2e-selenium
```

### Abrir en el navegador

http://localhost:7900

conectar al servicio, para ver los procesos e2e es necesario volver a correr las pruebas

```bash
sudo docker compose run --rm e2e-selenium
```
---

### 📋 3. Pruebas de Performance
Ubicación: `./perf-tests`

### Descripción

Pruebas de carga y stress con Locust sobre:

- JSONPlaceholder
- - GET /posts
- - 100 usuarios, spawn rate 10, duración 2 min
- ReqRes
- - GET /api/users?page=2
- - 50 usuarios, spawn rate 5, duración 2 min
- Swagger Petstore
- - GET /v2/pet/findByStatus?status=available
- - 200 usuarios, spawn rate 10, duración 1 min
- Resultados exportados en CSV con métricas:
- - Tiempo de respuesta promedio y p95
- - Throughput (req/s)
- - Tasa de errores

### Cómo ejecutar

Para correr cada escenario se usa:

JSONPlaceholder
```bash
docker compose run --rm locust-json
```

ReqRes
```bash
docker compose run --rm locust-reqres
```

Petstore
```bash
docker compose run --rm locust-petstore
```

### Visualizar resultadoss

Los reportes CSV se guardan en:

`perf-tests/results/`
