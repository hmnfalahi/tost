from datetime import date

from sqlalchemy import Column, String, Date, Integer, select, func, extract
from sqlalchemy.orm import column_property, relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class Member(DeclarativeBase):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    birth_date = Column(Date, default=date.today())
    bots = relationship(
        'Bot',
        back_populates='owner',
        cascade="all, delete"
    )
    channels = relationship(
        'Channel',
        secondary='channel_admin',
        back_populates='admins',
        cascade="all, delete",
    )

    members_count = column_property(select([func.count(id)]))
    fullname = column_property(first_name + ' ' + last_name)
    age = column_property(date.today().year - extract('year', birth_date))

