import json
from typing import TypeVar

from deta import Deta

from app.backends.base import EmailBackend
from app.core.config import Settings, settings
from app.schemas import Timestamped

deta = Deta(settings.DETA_PROJECT_KEY)
db = deta.Base(settings.DETA_BASE_NAME)
ModelType = TypeVar("ModelType", bound=Timestamped)
EmailBackendType = TypeVar("EmailBackendType", bound=EmailBackend)


def get_email_backend(settings: Settings) -> EmailBackendType:
    pass


def save_model_to_db(instance: ModelType) -> None:
    data = instance.json()
    db.put(json.loads(data))
