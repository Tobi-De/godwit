from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import (
    MailingList,
    MailingListCreate,
    Message,
    MessageCreate,
    Subscriber,
    SubscriberCreate,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/message", response_model=Message)
async def create_message(message_in: MessageCreate):
    pass


@router.get("/message", response_model=List[Message])
async def read_messages(skip: int = 0, limit: int = 100):
    pass


@router.get("/message/{key}", response_model=Message)
async def read_message(key: str):
    pass


@router.post("/mailing-list", response_model=MailingList)
async def create_mailing_list(mailing_list_in: MailingListCreate):
    pass


@router.get("/mailing-list", response_model=List[MailingList])
async def read_all_mailing_list(
        skip: int = 0, limit: int = 100
):
    pass


@router.get("/mailing-list/{key}", response_model=MailingList)
async def read_mailing_list(key: str):
    pass


@router.post("/subscriber", response_model=Subscriber)
async def create_subscriber(message_in: SubscriberCreate):
    pass


@router.get("/subscriber", response_model=List[Subscriber])
async def read_subscribers(skip: int = 0, limit: int = 100):
    pass


@router.get("/subscriber/{key}", response_model=Subscriber)
async def read_subscriber(key: str):
    pass
