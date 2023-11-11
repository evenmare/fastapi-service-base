import typing

from fastapi import APIRouter
from pydantic import BaseModel

from api.main import API_V1_PREFIX

service_info_router = APIRouter(
    prefix=API_V1_PREFIX,
    tags=['service-info']
)


class HealthResponseSchema(BaseModel):
    """ Описание ответа на запрос получения здоровья """
    status: typing.Literal['ok']


@service_info_router.get('/health', response_model=HealthResponseSchema)
async def get_service_health():
    """ Получение здоровья сервиса """
    return {'status': 'ok'}
