from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CaseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    court: Optional[str] = Field(default=None, max_length=200)
    case_number: Optional[str] = Field(default=None, max_length=100)
    case_type: Optional[str] = Field(default=None, max_length=100)
    facts: Optional[str] = None


class CaseResponse(BaseModel):
    id: int
    title: str
    court: Optional[str] = None
    case_number: Optional[str] = None
    case_type: Optional[str] = None
    facts: Optional[str] = None
    created_at: datetime


class PartyCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    role: str = Field(min_length=1, max_length=100)
    address: Optional[str] = None
    phone: Optional[str] = None


class FactCreate(BaseModel):
    description: str = Field(min_length=1)
    event_date: Optional[datetime] = None


class EvidenceCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    evidence_type: Optional[str] = None


class MemoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)
    memo_type: Optional[str] = None


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    due_date: Optional[datetime] = None
    completed: bool = False
