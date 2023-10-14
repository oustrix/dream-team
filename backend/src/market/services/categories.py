from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.market import tables
from src.market.database import get_session


class CategoriesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_categories(self) -> List[tables.Category]:
        categories = (
            self.session
            .query(tables.Category)
            .all()
        )

        return categories
