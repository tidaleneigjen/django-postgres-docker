# Django + Postgres + Docker Boilerplate

This project is a minimal Django setup running with Postgres in Docker.

![CI](https://github.com/tidaleneigjen/django-postgres-docker/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/tidaleneigjen/django-postgres-docker/branch/main/graph/badge.svg)](https://codecov.io/gh/tidaleneigjen/django-postgres-docker)

## 🚀 Quickstart

### 1. Clone and Setup
```bash
git clone https://github.com/tidaleneigjen/django-postgres-docker.git
cd django-postgres-docker
```

### 2. Create a .env file
```bash
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
```

### 3. Run with docker
```bash
docker compose up --build
```

This app will be available at http://localhost:8000.

## Misc

### Database
Postgres runs in a container and persists data in the pgdata/ volume.


### To run a django shell inside the docker container:
```bash
docker compose exec backend python manage.py shell
```

### To run a django shell inside the docker container:
```bash
docker compose exec backend python manage.py shell_plus
```

### To run bash inside the docker container
```bash
docker compose exec backend bash
```
