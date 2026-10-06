from app.core.config import settings

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.database_url)

session_maker = async_sessionmaker(bind = engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_session():
    async with session_maker() as session:
        yield session
