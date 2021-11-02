from typing import Optional

from pydantic import EmailStr

from app.schemas import Subscriber

from .base import EmailBackend


class SmtpEmailBackend(EmailBackend):
    def send_message(
            self,
            message: str,
            recipient_list: list[Subscriber],
            from_email: Optional[EmailStr] = None,
    ):
        pass
