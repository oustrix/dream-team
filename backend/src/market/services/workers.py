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
        query = self.session.query(tables.Worker)

        if amount:
            query.limit(amount)

        workers = query.all()

        return workers