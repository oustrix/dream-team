from typing import List

from fastapi import APIRouter, Depends

from src.market.services.categories import CategoriesService
from src.market.tables import Category

router = APIRouter(
    prefix='/categories',
    tags=['categories']
)


@router.get('/', response_model=List[Category], summary='Получение категорий')
def get_categories(
        service: CategoriesService = Depends()
):
    """
    Получнеие списка категорий.
    \f
    :param service:
    :return:
    """
    return service.get_categories()
