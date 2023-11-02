from fastapi import APIRouter

from .operations import router as operations_router
from .auth import router as auth_router
from .orders import router as orders_router
from .responses import router as responses_router
from .categories import router as categories_router
from .workers import router as workers_router
from .paybacks import router as paybacks_router

router = APIRouter()
router.include_router(operations_router)
router.include_router(auth_router)
router.include_router(orders_router)
router.include_router(responses_router)
router.include_router(categories_router)
router.include_router(workers_router)
router.include_router(paybacks_router)