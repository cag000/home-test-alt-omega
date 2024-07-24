import platform
import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routers import author_http, book_http, author_rpc, book_rpc
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from app.infrastructure.db.database import db_engine, primary_database
from app.common.env_loader import EnvLoader
from app.infrastructure.cache.redis_cache import RedisCache

# Load environment variables
env = EnvLoader()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await primary_database.connect()
    yield
    # Shutdown
    await primary_database.disconnect()


app = FastAPI(lifespan=lifespan)

# Initialize dependencies
db_engine
cache = RedisCache()

# Instrument the application for OpenTelemetry
FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=db_engine.engine)

# Include routers
app.include_router(author_http.router, prefix="/authors", tags=["authors"])
app.include_router(book_http.router, prefix="/books", tags=["books"])
# app.include_router(author_rpc.router, prefix="/rpc/authors", tags=["rpc_authors"])
# app.include_router(book_rpc.router, prefix="/rpc/books", tags=["rpc_books"])

if __name__ == "__main__":
    import uvicorn

    if platform.system() != "Windows":
        import uvloop

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    else:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
