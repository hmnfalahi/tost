from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class Event(DeclarativeBase):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    description = Column(String)
    bot_id = Column(Integer, ForeignKey('bot.id', ondelete="CASCADE"))
    channel_id = Column(Integer, ForeignKey('channel.id', ondelete="CASCADE"))

    bot = relationship(
        'Bot',
        back_populates='event',
        uselist=False,
        cascade="all, delete",
    )
    channel = relationship(
        'Channel',
        back_populates='event',
        uselist=False,
        cascade="all, delete",
    )

    @hybrid_property
    def owner(self):
        return self.bot or self.channel


