
from fastapi import APIRouter, Depends, HTTPException, status
import reflex as rx

from pcweb.utils import signup_for_newsletter

router = APIRouter()

class NewsLetterRequest(rx.Base):
    """Params for apps creation endpoint."""
    email: str


@router.post("/api/newsletter/signup", status_code=status.HTTP_201_CREATED)
async def news_letter_signup(news_letter_params: NewsLetterRequest):
    errors = signup_for_newsletter(news_letter_params.email)
    if errors is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errors)
    return news_letter_params
