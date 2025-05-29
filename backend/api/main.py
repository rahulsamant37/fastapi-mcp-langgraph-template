from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import llms


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan, swagger_ui_parameters={"tryItOutEnabled": True}
)
app.include_router(llms.router, prefix="/v1")
