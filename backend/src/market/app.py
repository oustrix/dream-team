from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    },
    {
        'name': 'responses',
        'description': 'Операции с откликами',
    },
    {
        'name': 'categories',
        'description': 'Операции с категориями',
    },
    {
        'name': 'workers',
        'description': 'Операции с работниками'
    }
]

app = FastAPI(
    title='Market',
    description='Биржа фриланса',
    version='1.0.0',
    openapi_tags=tags_metadata
)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)