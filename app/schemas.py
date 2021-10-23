from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Timestamped(BaseModel):
    created: datetime = Field(default_factory=datetime.now)


class Subscriber(Timestamped):
    name: str
    email: EmailStr


class MailingList(Timestamped):
    name: str
    subscribers: list[Subscriber]


class Message(Timestamped):
    class Status(str, Enum):
        SENT = "Sent"

    subject: str
    content: str
    html_content: Optional[str] = None
    status: Status = Status.SENT
