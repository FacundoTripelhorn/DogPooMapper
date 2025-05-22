from fastapi import FastAPI
from .core.config import get_settings
from .api.endpoints import events
from .models.event import SQLModel  # ensure model discovery
from .core.database import engine

SQLModel.metadata.create_all(engine)

settings = get_settings()
app = FastAPI(title="Dog Poop Map API", openapi_url=f"{settings.api_prefix}/openapi.json")

app.include_router(events.router, prefix=settings.api_prefix)