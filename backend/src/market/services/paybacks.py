from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.market import tables
from src.market.database import get_session


class PaybacksService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_paybacks(self) -> List[tables.Payback]:
        categories = (
            self.session
            .query(tables.Payback)
            .all()
        )

        return categories