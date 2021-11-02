from typing import Any, Optional

from pydantic import BaseSettings, EmailStr, validator


class Settings(BaseSettings):
    DETA_PROJECT_KEY: str
    DETA_BASE_NAME: str = "godwit"
    EMAIL_VERIFICATION: bool = True
    FROM_EMAIL: EmailStr

    # SMTP
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    SMTP_ENABLED: bool = False

    @validator("SMTP_ENABLED", pre=True)
    def get_smtp_enabled(cls, _: bool, values: dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
        )

    # AMAZON SES
    AWS_ACCESS_KEY_ID: Optional[str]
    AWS_SECRET_ACCESS_KEY: Optional[str]

    SES_ENABLED: bool = False

    @validator("SES_ENABLED", pre=True)
    def get_ses_enabled(cls, _: bool, values: dict[str, Any]) -> bool:
        return bool(
            values.get("AWS_ACCESS_KEY_ID")
            and values.get("AWS_SECRET_ACCESS_KEY")
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
