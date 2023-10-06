from typing import List, Optional
from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.operations import OperationCreate, OperationKind
from .. import tables


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int, kind: Optional[OperationKind] = None) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        query.filter_by(user_id)

        if kind:
            query.filter_by(kind=kind)

        operations = query.all()

        return operations

    def create(self, user_id: int, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.model_dump())
        operation.date = datetime.utcnow()
        operation.user_id = user_id
        self.session.add(operation)
        self.session.commit()
        return operation
