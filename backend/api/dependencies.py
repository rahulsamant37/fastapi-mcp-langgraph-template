from typing import Annotated, Iterable

from fastapi import Depends
from langchain_openai import ChatOpenAI

from config import settings


def llm_factory() -> ChatOpenAI:
    llm = ChatOpenAI(
        streaming=True,
        model=settings.model,
        temperature=0,
        api_key=settings.openai_api_key,
        stream_usage=True,
    )
    return llm


def get_llm_session() -> Iterable[ChatOpenAI]:
    yield llm_factory()


LLMDep = Annotated[ChatOpenAI, Depends(get_llm_session)]
