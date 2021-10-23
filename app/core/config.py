from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    DETA_PROJECT_KEY: str
    DETA_BASE_NAME: str = "godwit"
    EMAIL_FROM: EmailStr
    SERVER_MAIL: EmailStr

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
