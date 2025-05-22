from contextlib import contextmanager
from sqlmodel import create_engine, Session
from pathlib import Path

from .config import get_settings

settings = get_settings()
db_path = Path(settings.db_url.replace("sqlite:///", ""))
db_path.parent.mkdir(parents=True, exist_ok=True)
engine = create_engine(settings.db_url, echo=False, connect_args={"check_same_thread": False})

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session