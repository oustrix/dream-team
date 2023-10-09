from datetime import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.market.database import get_session
from src.market.models.auth import User
from src.market import tables
from src.market.models.responses import ResponseCreate


class ResponsesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_responses(self, order_id: int, user: User) -> List[tables.Response]:
        exception_not_user_order = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="It is forbidden to decline in process order",
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )

        order = (
            self.session
            .query(tables.Order)
            .filter_by(id=order_id)
            .first()
        )

        if order.owner_id != user.id:
            raise exception_not_user_order from None

        responses = (
            self.session
            .query(tables.Response)
            .filter_by(order_id=order.id)
            .all()
        )

        return responses

    def create_response(self, user: User, response_data: ResponseCreate) -> tables.Response:
        response = tables.Response(**response_data.model_dump())
        response.user_id = user.id
        response.created_at = datetime.utcnow()

        self.session.add(response)
        self.session.commit()

        return response
