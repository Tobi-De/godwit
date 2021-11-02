from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router

description = """
Send mails to your subscribers.
....
"""


def get_application():
    _app = FastAPI(title="godwit", description=description)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.include_router(router)
