from fastapi import FastAPI

from .api import router

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'operations',
        'description': 'Операции со счётом'
    },
    {
        'name': 'orders',
        'description': 'Операции с заказами'
    }
]

app = FastAPI(
    title='Market',
    description='Биржа фриланса',
    version='1.0.0',
    openapi_tags=tags_metadata
)
app.include_router(router)