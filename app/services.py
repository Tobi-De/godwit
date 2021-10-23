import json
from typing import TypeVar

from deta import Deta

from .core.config import settings
from .schemas import Timestamped, Message, Subscriber

deta = Deta(settings.DETA_PROJECT_KEY)
db = deta.Base(settings.DETA_BASE_NAME)
ModelType = TypeVar("ModelType", bound=Timestamped)


def save_model_to_db(instance: ModelType) -> None:
    data = instance.json()
    db.put(json.loads(data))


def send_mail(message: Message, recipient_list: list[Subscriber]):
    pass
