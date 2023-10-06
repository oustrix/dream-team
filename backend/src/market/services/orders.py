from datetime import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.market import tables
from src.market.database import get_session
from src.market.models.auth import User
from src.market.models.orders import OrderCreate, OrderStatus


class OrdersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_order(self, order_id: int) -> tables.Order:
        order = (
            self.session
            .query(tables.Order)
            .filter_by(id=order_id)
            .first()
        )

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='order not found'
            )

        return order

    # TODO: make filters
    def get_orders(self) -> List[tables.Order]:
        orders = (
            self.session
            .query(tables.Order)
            .all()
        )

        return orders

    def create_order(self, order_data: OrderCreate, user_data: User) -> tables.Order:
        order = tables.Order(**order_data.model_dump())
        order.owner_id = user_data.id
        order.status = OrderStatus.OPEN
        order.created_at = datetime.utcnow()

        self.session.add(order)
        self.session.commit()

        return order
