# Backend FastAPI and MySQL - Base Project

```bash
python3.9 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/uvicorn app:app --reload
```
***
### Migrations
- create a new revision (autogenerate)
```bash
venv/bin/alembic revision --autogenerate
```
- run migration
```bash
venv/bin/alembic upgrade head
```
***
