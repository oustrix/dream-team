from typing import List

from fastapi import APIRouter, Depends

from src.market.models.paybacks import Payback
from src.market.services.paybacks import PaybacksService

router = APIRouter(
    prefix='/paybacks',
    tags=['paybacks']
)

@router.get('/', response_model=List[Payback], summary='Получение методов оплаты')
def get_paybacks(
        service: PaybacksService = Depends()
):
    """
    Получение списка методов возможной оплаты.
    \f
    :return:
    """
    return service.get_paybacks()