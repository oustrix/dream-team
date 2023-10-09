from datetime import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.market import tables
from src.market.database import get_session
from src.market.models.auth import User
from src.market.models.orders import OrderCreate, OrderStatus, OrderUpdate


def process_open_order(old_data: tables.Order, new_data: OrderUpdate) -> tables.Order:
    order = old_data

    if new_data.worker_id is not None:
        order.worker_id = new_data.worker_id
        order.status = OrderStatus.IN_PROCESS
        order.assigned_at = datetime.utcnow()

    elif new_data.status == OrderStatus.DECLINED or new_data.status == OrderStatus.CLOSED:
        order.status = OrderStatus.DECLINED
        order.closed_at = datetime.utcnow()

    else:
        for key, value in new_data:
            setattr(order, key, value)

    return order


def process_inprocess_order(old_data: tables.Order, new_data: OrderUpdate) -> tables.Order:
    order = old_data


class OrdersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, order_id: int) -> tables.Order:
        order = (
            self.session
            .query(tables.Order)
            .filter_by(id=order_id)
            .first()
        )

        return order

    def get_order(self, order_id: int) -> tables.Order:
        order = self._get(order_id)

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Order not found'
            )

        return order

    def get_orders(self,
                   order_status: OrderStatus = None,
                   owner_id: int = None,
                   worker_id: int = None) -> List[tables.Order]:
        query = self.session.query(tables.Order)

        if order_status:
            query.filter_by(status=order_status)
        if owner_id:
            query.filter_by(owner_id=owner_id)
        if worker_id:
            query.filter_by(worker_id=worker_id)

        orders = query.all()

        return orders

    def create_order(self, order_data: OrderCreate, user_data: User) -> tables.Order:
        order = tables.Order(**order_data.model_dump())
        order.owner_id = user_data.id
        order.status = OrderStatus.OPEN
        order.created_at = datetime.utcnow()

        self.session.add(order)
        self.session.commit()

        return order
