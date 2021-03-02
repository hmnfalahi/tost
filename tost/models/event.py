from sqlalchemy import Integer, ForeignKey, String, Enum
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


STATUSES = [
    'draft',
    'published',
    'expired',
]


class Event(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    __tablename__ = 'event'

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
    title = Field(
        String(50),
        unique=True,
        required=True,
        not_none=True,
        readonly=False,
        label='Title',
        example='EventTitle',
    )
    status = Field(
        Enum(*STATUSES, name='statuses'),
        python_type=str,
        not_none=True,
        required=True,
        readonly=False,
        label='status',
        watermark='Choose Event Status',
        example='draft',
    )
    description = Field(
        String(50),
        unique=False,
        required=False,
        not_none=False,
        readonly=False,
        label='Description',
        example='event description',
    )
    bot_id = Field(
        Integer, ForeignKey('bot.id'),
        python_type=int,
        watermark='Choose an bot',
        label='Bot Id',
        nullable=True,
        not_none=False,
        readonly=True,
    )
    channel_id = Field(
        Integer, ForeignKey('channel.id'),
        python_type=int,
        watermark='Choose an channel',
        label='Channel Id',
        nullable=True,
        not_none=False,
        readonly=True,
    )
    creator_id = Field(
        Integer, ForeignKey('member.id'),
        python_type=int,
        watermark='Choose an Member',
        label='Member Id',
        required=True,
        nullable=False,
        not_none=False,
        readonly=True,
    )
    creator = relationship(
        'Member',
        back_populates='events',
        uselist=False,
        cascade='all, delete',
    )
    bot = relationship(
        'Bot',
        back_populates='events',
        uselist=False,
        cascade='all, delete',
    )
    channel = relationship(
        'Channel',
        back_populates='events',
        uselist=False,
        cascade='all, delete',
    )

    @hybrid_property
    def owner(self):
        return self.bot or self.channel

