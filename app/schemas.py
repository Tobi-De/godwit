from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from .core.config import settings


class Timestamped(BaseModel):
    created: datetime = Field(default_factory=datetime.now)


class SubscriberBase(Timestamped):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    extra: Optional[dict] = Field(default_factory=dict)
    verified: bool = False


class SubscriberCreate(SubscriberBase):
    name: str
    email: EmailStr


class Subscriber(SubscriberBase):
    key: str


class MailingListBase(Timestamped):
    name: Optional[str] = None
    subscribers: Optional[list[Subscriber]] = Field(default_factory=list)
    from_email: Optional[EmailStr] = settings.FROM_EMAIL


class MailingListCreate(MailingListBase):
    name: str


class MailingList(MailingListBase):
    key: str


class MessageBase(Timestamped):
    class Status(str, Enum):
        NEW = "NEW"
        SENT = "SENT"

    subject: Optional[str] = None
    content: Optional[str] = None
    html_content: Optional[str] = None
    status: Status = Status.SENT
    from_email: Optional[EmailStr] = settings.FROM_EMAIL


class MessageCreate(MessageBase):
    subject: str
    content: str


class Message(MessageBase):
    key: str
