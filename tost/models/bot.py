from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class Bot(DeclarativeBase):
    __tablename__ = 'bot'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey('member.id', ondelete="CASCADE"))

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

