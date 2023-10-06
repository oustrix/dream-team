from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends

from ..models.auth import User
from ..models.operations import Operation, OperationCreate, OperationKind
from ..services.auth import get_current_user
from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/', response_model=List[Operation])
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


@router.post('/', response_model=List[Operation], summary='Создание операции')
def create_operation(
        operation_data: OperationCreate,
        service: OperationsService = Depends(),
        user: User = Depends(get_current_user)
):
    """
    Создание новой операции.

    - **kind**: тип операции (см. схему OperationKind)
    - **amount**: сумма операции
    - **description**: описание операции (необязательно)
    \f
    :param operation_data:
    :param service:
    :param user:
    :return:
    """
    return service.create(user.id, operation_data)
