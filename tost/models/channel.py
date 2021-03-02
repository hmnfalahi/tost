from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class ChannelAdmin(DeclarativeBase):
    __tablename__ = 'channel_admin'

    channel_id = Field(
        Integer,
        ForeignKey('channel.id'),
        primary_key=True
    )
    admin_id = Field(
        Integer,
        ForeignKey('member.id'),
        primary_key=True
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

    admins = relationship(
        'Member',
        secondary='channel_admin',
        back_populates='channels',
        cascade="all, delete",
    )
    events = relationship(
        'Event',
        back_populates='channel',
        cascade="all, delete",
    )

