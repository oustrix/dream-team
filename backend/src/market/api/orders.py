from typing import List, Optional

from fastapi import APIRouter, Depends

from src.market.models.auth import User
from src.market.models.orders import Order, OrderCreate, OrderStatus
from src.market.services.auth import get_current_user
from src.market.services.orders import OrdersService

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@router.get('/', response_model=List[Order])
def get_orders(
        status: Optional[OrderStatus] = None,
        owner: int = None,
        worker: int = None,
        service: OrdersService = Depends()
):
    """
    Получение списка заказов.

    - **status**: статус заказаа (см. схему OrderStatus)
    - **owner**: ID владельца заказа
    - **worker**: ID исполнителя заказа

    \f
    :param status:
    :param owner:
    :param worker:
    :param service:
    :return:
    """
    return service.get_orders(status=status, owner_id=owner, worker_id=worker)


@router.get('/{order_id}', response_model=Order)
def get_order(
        order_id: int,
        service: OrdersService = Depends(),
):
    return service.get_order(order_id)


@router.post('/', response_model=Order)
def create_order(
        order_data: OrderCreate,
        user: User = Depends(get_current_user),
        service: OrdersService = Depends(),
):
    return service.create_order(order_data, user)
