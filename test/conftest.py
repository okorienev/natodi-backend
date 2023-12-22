import asyncio
import logging
from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import text

import alembic.config
from app.database import async_engine
from app.main import app

PYTEST_OPTION = None

log = logging.getLogger(__name__)


def pytest_configure(config):
    global PYTEST_OPTION
    PYTEST_OPTION = config.option


def pytest_sessionstart(session):
    if PYTEST_OPTION.collectonly:
        return

    wait_for_database_startup()
    run_migrations()


def run_migrations():
    alembic_args = ["--raiseerr", "upgrade", "head"]

    alembic.config.main(argv=alembic_args)


def wait_for_database_startup():
    print("Waiting for database startup")

    async def _wait():
        async with async_engine.connect() as conn:
            for _ in range(10):
                try:
                    await conn.execute(text("SELECT VERSION();"))
                    print("Database is up and running")
                    return
                except Exception as e:  # noqa
                    print("Database starting up")
                    await asyncio.sleep(2)

        print("Database failed to start in 20 seconds")

    asyncio.run(_wait())


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test-server") as test_client:
        yield test_client
