from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from ...core.database import get_session
from ...models.event import PoopEvent
from ...schemas.event import PoopEventCreate, PoopEventRead

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/", response_model=PoopEventRead)
def create_event(payload: PoopEventCreate, session=Depends(get_session)):
    event = PoopEvent.from_orm(payload)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event

@router.get("/", response_model=List[PoopEventRead])
def list_events(session=Depends(get_session)):
    return session.exec(select(PoopEvent)).all()