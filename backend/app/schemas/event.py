from datetime import datetime
from pydantic import BaseModel

class PoopEventCreate(BaseModel):
    dog_id: str
    timestamp: datetime
    x: float
    y: float

class PoopEventRead(PoopEventCreate):
    id: int