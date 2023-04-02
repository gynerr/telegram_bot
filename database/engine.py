from sqlalchemy import URL, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker


def create_async_eng(url: URL | str) -> AsyncEngine:
    return create_async_engine(url=url, echo=True, pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return async_sessionmaker(engine, expire_on_commit=False)
