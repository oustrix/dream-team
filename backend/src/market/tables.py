import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        sa.CheckConstraint('balance >= 0'),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String, unique=True)
    name = sa.Column(sa.String(31))
    surname = sa.Column(sa.String(31))
    photo = sa.Column(sa.String(255))
    balance = sa.Column(sa.Numeric(10, 2), default=0)
    pending_money = sa.Column(sa.Numeric(10, 2), default=0)
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
    category_id = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))
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


class Response(Base):
    __tablename__ = 'responses'

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    description = sa.Column(sa.Text)
    created_at = sa.Column(sa.Date)


class Category(Base):
    __tablename__ = 'categories'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class Worker(Base):
    __tablename__ = 'workers'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    main_category = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))

class Payback(Base):
    __tablename__ = 'paybacks'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(31))
    count = sa.Column(sa.Integer)
    units = sa.Column(sa.String(31))
    price = sa.Column(sa.Integer)