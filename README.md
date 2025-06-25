# Django + Postgres + Docker Boilerplate

A minimal Django setup running with PostgreSQL in Docker. Ideal for starting new projects with clean, tested, containerized foundations.

---

## 🔧 Badges

![CI](https://github.com/tidaleneigjen/django-postgres-docker/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/tidaleneigjen/django-postgres-docker/branch/main/graph/badge.svg)](https://codecov.io/gh/tidaleneigjen/django-postgres-docker)
![Docker Build](https://github.com/tidaleneigjen/django-postgres-docker/actions/workflows/docker-build.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/tidaleneigjen/django-postgres-docker)

---

## 🚀 Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/tidaleneigjen/django-postgres-docker.git
cd django-postgres-docker
```

### 2. Create a `.env` file
Add the following:
```env
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
```

### 3. Run the project
```bash
docker compose up --build
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Running Tests

Run the full test suite with coverage:

```bash
docker compose exec backend coverage run manage.py test
docker compose exec backend coverage report
```

Or simply:

```bash
docker compose exec backend python manage.py test
```

> ✅ Tests are run automatically in CI and tracked with Codecov.

---

## 🐚 Useful Commands

### Django Shell
```bash
docker compose exec backend python manage.py shell
```

### Django Shell Plus (with model auto-imports)
```bash
docker compose exec backend python manage.py shell_plus
```

### Bash inside backend container
```bash
docker compose exec backend bash
```

---

## 🗃️ Database Info

- PostgreSQL runs in a container
- Data persists in a named Docker volume: `pgdata`
- Connection parameters are configurable via `.env`

---

## 📦 DockerHub

This image is automatically built and published to [DockerHub](https://hub.docker.com/r/tidaleneigjen/django-postgres-docker) on push to `main`.

