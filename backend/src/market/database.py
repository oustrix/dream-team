from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.database_url,
    pool_reset_on_return=None,
)

session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
