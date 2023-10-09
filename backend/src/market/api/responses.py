from typing import List

from fastapi import APIRouter, Depends

from src.market.models.auth import User
from src.market.models.responses import Response, ResponseCreate
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


@router.post('/', response_model=Response, summary='Создание отклика')
def create_response(
        response_data: ResponseCreate,
        user: User = Depends(get_current_user),
        service: ResponsesService = Depends()
):
    """
    Создание нового отклика.

    - **order_id**: ID заказа, к которому оставлен отклик.
    - **description**: комментарий к отклику.

    \f
    :param response_data:
    :param user:
    :param service:
    :return:
    """
    return service.create_response(user, response_data)
