spin-up services app is dependant on:
```shell
docker-compose up -d
```

generate .env file from settings:
```shell
python -m cli dotenv generate
```

Run app
```shell
uvicorn app.main:app --reload
```

### Migrations
update database:
```shell
alembic upgrade head
```

downgrade database version by 1
```shell
alembic downgrade -1
```

generate new version (when editing models)
```shell
alembic revision --autogenerate -m <your_revision_slug>
```