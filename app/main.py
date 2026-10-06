from app.database.db import engine
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.db import Base
from app.api.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as engine_session:
        await engine_session.run_sync(Base.metadata.create_all)

    yield 

    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
