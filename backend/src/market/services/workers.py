from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.market import tables


class WorkersService:
    def __init__(self, session: Session = Depends()):
        self.session = session

    def get_workers(self,
                    amount: int = None) -> List[tables.Worker]:
        query = self.session.query(tables.Worker)

        workers: List[tables.Worker]
        if amount:
            workers = query.count(amount)
        else:
            workers = query.all()

        return workers