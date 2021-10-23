from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

description = """
# Descriptions
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
