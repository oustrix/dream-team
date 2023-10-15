from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.market import tables
from src.market.database import get_session


class WorkersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_workers(self,
                    amount: int = None) -> List[tables.Worker]:
        query = (
            self.session.query(tables.Worker.id,
                               tables.Worker.user_id,
                               tables.Worker.main_category,
                               tables.Category.name,
                               tables.User.photo,
                               tables.User.name,
                               tables.User.surname)
            .join(tables.User, tables.Worker.user_id == tables.User.id)
            .outerjoin(tables.Category, tables.Worker.main_category == tables.Category.id)
        )

        if amount:
            query.limit(amount)

        workers = query.all()

        return workers
