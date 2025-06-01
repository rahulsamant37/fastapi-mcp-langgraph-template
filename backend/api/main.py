from fastapi import FastAPI

from api.routers import checkpoints, llms, mcps

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
app.include_router(llms.router, prefix="/v1")
app.include_router(mcps.router, prefix="/v1")
app.include_router(checkpoints.router, prefix="/v1")
