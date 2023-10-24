from typing import List, Optional

from fastapi import APIRouter, Depends

from src.market.models.auth import User
from src.market.models.orders import Order, OrderCreate, OrderStatus, OrderUpdate
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
        amount: int = None,
        category: int = None,
        service: OrdersService = Depends()
):
    """
    Получение списка заказов.

    - **status**: статус заказаа (см. схему OrderStatus)
    - **owner**: ID владельца заказа
    - **worker**: ID исполнителя заказа
    - **amount**: количество заказов
    - **category**: ID категории

    \f
    :param category:
    :param amount:
    :param status:
    :param owner:
    :param worker:
    :param service:
    :return:
    """
    return service.get_orders(order_status=status, owner_id=owner, worker_id=worker, amount=amount, category_id=category)



@router.get('/{order_id}', response_model=Order, summary="Получение заказа")
def get_order(
        order_id: int,
        service: OrdersService = Depends(),
):
    """
    Получение заказа.

    - **order_id**: ID заказа.

    \f
    :param order_id:
    :param service:
    :return:
    """
    return service.get_order(order_id)


@router.post('/', response_model=Order, summary='Создание заказа')
def create_order(
        order_data: OrderCreate,
        user: User = Depends(get_current_user),
        service: OrdersService = Depends(),
):
    """
    Первичное создание заказа.

    - **title**: название заказа
    - **description**: длинное описание заказа
    - **reward**: сумма заказа

    \f
    :param order_data:
    :param user:
    :param service:
    :return:
    """
    return service.create_order(order_data, user)


@router.put('/{order_id}', response_model=Order, summary='Обновление заказа')
def update_order(
        order_id: int,
        update_data: OrderUpdate,
        user: User = Depends(get_current_user),
        service: OrdersService = Depends()
):
    """
    Обновление информации о заказе.


    :param order_id:
    :param update_data:
    :param user:
    :param service:
    :return:
    """
    return service.update_order(order_id, user, update_data)