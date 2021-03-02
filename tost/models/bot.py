from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class Bot(DeclarativeBase):
    __tablename__ = 'bot'

    id = Field(
        Integer,
        primary_key=True,
        unique=True,
        required=True,
        not_none=True,
        readonly=True,
        label='ID',
        minimum=1,
    )
    name = Field(
        String(50),
        unique=True,
        required=True,
        not_none=True,
        readonly=False,
        label='Name',
        example='AliBot',
    )
    title = Field(
        String(50),
        unique=False,
        required=False,
        not_none=True,
        readonly=False,
        label='Title',
        example='AliBot',
    )
    owner_id = Field(
        Integer,
        ForeignKey('member.id'),
        python_type=int,
        watermark='Choose an owner',
        label='Owner Id',
        nullable=False,
        not_none=True,
        readonly=True,
    )

    owner = relationship(
        'Member',
        back_populates='bots',
        cascade="all, delete",
    )
    events = relationship(
        'Event',
        back_populates='bot',
        cascade="all, delete",
    )

