from typing import List

from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import Operation, OperationCreate
from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
)


@router.get('/', response_model=List[Operation])
def get_operations(
        service: OperationsService = Depends()
):
    return service.get_list()


@router.post('/', response_model=List[Operation])
def create_operation(
        operation_data: OperationCreate,
        service: OperationsService = Depends(),
):
    return service.create(operation_data)
