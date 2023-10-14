from typing import Optional

from fastapi import APIRouter, Depends

from src.market.models.workers import Worker
from src.market.services.workers import WorkersService

router = APIRouter(
    prefix='/workers',
    tags=['workers']
)


@router.get('/', response_model=Worker, summary='Получение исполнителей')
def get_workers(
        amount: Optional[int] = None,
        service: WorkersService = Depends()
):
    return service.get_workers(amount)