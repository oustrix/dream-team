import uvicorn

from .settings import settings

if __name__ == '__main__':
    uvicorn.run('src.market.app:app',
                host=settings.server_host,
                port=settings.server_port,
                reload=True)
