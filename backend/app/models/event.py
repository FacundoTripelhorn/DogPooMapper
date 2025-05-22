from datetime import datetime
from sqlmodel import SQLModel, Field

class PoopEvent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    dog_id: str
    timestamp: datetime
    x: float
    y: float