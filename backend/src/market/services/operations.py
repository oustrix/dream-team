from typing import List
from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.operations import OperationCreate
from .. import tables


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int) -> List[tables.Operation]:
        operations = (
            self.session
            .query(tables.Operation)
            .filter_by(user_id=user_id)
            .all()
        )

        return operations

    def create(self, user_id: int, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.model_dump())
        operation.date = datetime.utcnow()
        operation.user_id = user_id
        self.session.add(operation)
        self.session.commit()
        return operation
