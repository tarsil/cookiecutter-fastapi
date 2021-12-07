import asyncpg
from fastapi import FastAPI
from loguru import logger

from ...conf import settings


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {}", repr(settings.database_url))

    app.state.pool = await asyncpg.create_pool(
        str(settings.database_url),
        min_size=settings.min_connection_count,
        max_size=settings.max_connection_count,
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")
