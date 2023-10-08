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
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)


class Order(Base):
    __tablename__ = 'orders'

    id = sa.Column(sa.Integer, primary_key=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    status = sa.Column(sa.String)
    worker_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    title = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    reward = sa.Column(sa.Numeric(10, 2))
    created_at = sa.Column(sa.Date)
    assigned_at = sa.Column(sa.Date)
    closed_at = sa.Column(sa.Date)


class Retention(Base):
    __tablename__ = 'retentions'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.id'))
    amount = sa.Column(sa.Numeric(10, 2))
    created_at = sa.Column(sa.Date)
    deleted_at = sa.Column(sa.Date)
