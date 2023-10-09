from typing import List

from fastapi import APIRouter, Depends

from src.market.models.auth import User
from src.market.models.responses import Response
from src.market.services.auth import get_current_user
from src.market.services.responses import ResponsesService

router = APIRouter(
    prefix='/responses',
    tags=['responses']
)


@router.get('/{order_id}', response_model=List[Response], summary='Получение откликов')
def get_responses(
        order_id: int,
        user: User = Depends(get_current_user),
        service: ResponsesService = Depends()
):
    """
    Получение всех отклков на заказ.

    - **order_id**: ID заказа
    \f
    :param order_id:
    :param user:
    :param service:
    :return:
    """
    return service.get_responses(order_id, user)
