from fastapi import FastAPI
from contextlib import asynccontextmanager
import redis.asyncio as redis

# IMPORT CHECK: If this fails, the environment is wrong.
from cco_core import __name__ as core_name

# Setup Redis connection lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to Redis (URL from Docker env var)
    app.state.redis = redis.from_url("redis://redis:6379", encoding="utf-8", decode_responses=True)
    yield
    # Shutdown: Close connection
    await app.state.redis.close()

app = FastAPI(title="CCO Generation Service", lifespan=lifespan)

@app.get("/")
async def health_check():
    """
    Verifies that:
    1. The API is running.
    2. The Core library is linked.
    3. Redis is accessible.
    """
    redis_status = "unknown"
    try:
        if await app.state.redis.ping():
            redis_status = "connected"
    except Exception as e:
        redis_status = f"error: {str(e)}"

    return {
        "service_status": "online",
        "core_library_linked": core_name, # Should return "cco_core"
        "redis_status": redis_status
    }
