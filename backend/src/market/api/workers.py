from typing import Optional, List

from fastapi import APIRouter, Depends

from src.market.models.workers import Worker
from src.market.services.workers import WorkersService

router = APIRouter(
    prefix='/workers',
    tags=['workers']
)


@router.get('/', response_model=List[Worker], summary='Получение исполнителей')
def get_workers(
        amount: Optional[int] = None,
        service: WorkersService = Depends()
):
    """
    Получение списка исполнителей.

    - **amount**: количество работников
    \f
    :param amount:
    :param service:
    :return:
    """
    return service.get_workers(amount)
