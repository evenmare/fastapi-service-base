from fastapi import FastAPI

from api import service_info_router

app = FastAPI()

app.include_router(service_info_router)
