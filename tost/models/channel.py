from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class ChannelAdmin(DeclarativeBase):
    __tablename__ = 'channel_admin'

    channel_id = Column(
        Integer,
        ForeignKey('channel.id', ondelete="CASCADE"),
        primary_key=True,
    )
    admin_id = Column(
        Integer,
        ForeignKey('member.id', ondelete="CASCADE"),
        primary_key=True,
    )

    channel = relationship(
        'Channel',
        cascade="all, delete",
        uselist=False,
    )
    admin = relationship(
        'Member',
        cascade="all, delete",
        uselist=False,
    )


class Channel(DeclarativeBase):
    __tablename__ = 'channel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey('member.id', ondelete="CASCADE"))
    admins = relationship(
        'Member',
        secondary='channel_admin',
        back_populates='channels',
        cascade="all, delete",
    )

