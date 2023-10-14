from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends

from ..models.auth import User
from ..models.operations import Operation, OperationKind
from ..services.auth import get_current_user
from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/', response_model=List[Operation], summary='Получение операций')
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationsService = Depends(),
        user: User = Depends(get_current_user)
):
    """
    Получение списка операций.

    - **kind**: тип операции (см. схему OperationKind)
    \f
    :param kind:
    :param service:
    :param user:
    :return:
    """
    return service.get_list(user.id, kind=kind)