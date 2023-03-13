from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/", response_class=PlainTextResponse)
def index():
    return PlainTextResponse(content="Hello, world!")


@router.get("/health", response_class=PlainTextResponse)
def health():
    return PlainTextResponse(content="OK")
