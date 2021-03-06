import abc
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas import Subscriber


class EmailBackend(BaseModel, abc.ABC):
    @abc.abstractmethod
    def send_message(
            self,
            message: str,
            recipient_list: list[Subscriber],
            from_email: Optional[EmailStr] = None,
    ):
        pass
