import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Integer, unique=True)
    username = sa.Column(sa.Text, unique=True)
    role = sa.Column(sa.String)
    password_hash = sa.Column(sa.Text)


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)
