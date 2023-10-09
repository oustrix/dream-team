from datetime import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.market import tables
from src.market.database import get_session
from src.market.models.auth import User
from src.market.models.orders import OrderCreate, OrderStatus, OrderUpdate


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
        exception_not_enough_money = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough money",
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )

        if user_data.balance < order_data.reward:
            raise exception_not_enough_money from None

        order = tables.Order(**order_data.model_dump())
        order.owner_id = user_data.id
        order.status = OrderStatus.OPEN
        order.created_at = datetime.utcnow()
        self.session.add(order)

        user = tables.User(**user_data.model_dump())
        user.balance -= order.reward
        user.pending_money += order.reward
        self.session.add(user)

        retention = tables.Retention()
        retention.created_at = datetime.utcnow()
        retention.user_id = user.id
        retention.amount = order.reward
        retention.order_id = order.id
        self.session.add(retention)

        self.session.commit()

        return order

    def update_order(self, order_id: int, user: User, update_data: OrderUpdate) -> tables.Order:
        exception_wrong_user = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The order doesn't belong to this user",
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
        exception_wrong_status = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access to closed/declined orders is prohibited",
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )

        order = self._get(order_id)

        if order.owner_id != user.id:
            raise exception_wrong_user from None

        updated_order = tables.Order()
        if order.status == OrderStatus.OPEN:
            updated_order = self.process_open_order(user, order, update_data)
        elif order.stats == OrderStatus.IN_PROCESS:
            updated_order = self.process_inprocess_order(user, order, update_data)
        else:
            raise exception_wrong_status from None

        return updated_order

    def process_open_order(self, user: User, old_data: tables.Order, new_data: OrderUpdate) -> tables.Order:
        order = old_data

        if new_data.worker_id is not None:
            order.worker_id = new_data.worker_id
            order.status = OrderStatus.IN_PROCESS
            order.assigned_at = datetime.utcnow()
            self.session.add(order)

        elif new_data.status == OrderStatus.DECLINED or new_data.status == OrderStatus.CLOSED:
            now = datetime.utcnow()

            order.status = OrderStatus.DECLINED
            order.closed_at = now
            self.session.add(order)

            user.pending_balance -= order.reward
            user.balance += order.reward
            self.session.add(user)

            retention = (
                self.session
                .query(tables.Retention)
                .filter_by(order_id=order.id)
                .first()
            )
            retention.deleted_at = now
            self.session.add(retention)

        else:
            for key, value in new_data:
                setattr(order, key, value)
            self.session.add(order)

        self.session.commit()
        return order

    def process_inprocess_order(self, user: User, old_data: tables.Order, new_data: OrderUpdate) -> tables.Order:
        order = old_data

        if new_data.status == OrderStatus.CLOSED:
            now = datetime.utcnow()

            order.status = OrderStatus.CLOSED
            order.closed_at = now
            self.session.add(order)

            user.pending_balance -= order.rewared
            self.session.add(order)

            worker = (
                self.session
                .query(tables.User)
                .filter_by(id=order.worker_id)
                .first()
            )
            worker.balance += order.reward
            self.session.add(order)

            retention = (
                self.session
                .query(tables.Retention)
                .filter_by(order_id=order.id)
                .first()
            )
            retention.deleted_at = now
            self.session.add(retention)

        self.session.commit()
        return order
