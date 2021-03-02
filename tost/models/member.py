import os
import uuid
from datetime import date, datetime
from hashlib import sha256

from restfulpy.principal import JWTRefreshToken, JWTPrincipal
from sqlalchemy import String, Enum, Date, Integer, select, func, \
    extract, Unicode
from sqlalchemy.orm import column_property, relationship, synonym
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin

MEMBER_GENDER = [
    'male',
    'female',
    'other',
]


class Member(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    __tablename__ = 'member'

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
    first_name = Field(
        String(50),
        required=True,
        not_none=True,
        readonly=False,
        label='First Name',
        example='ali',
    )
    last_name = Field(
        String(50),
        required=True,
        not_none=True,
        readonly=False,
        label='Last Name',
        example='ahmadi',
    )
    gender = Field(
        Enum(*MEMBER_GENDER, name='member_gender'),
        python_type=str,
        not_none=False,
        required=True,
        readonly=False,
        label='gender',
        watermark='Choose Your Gender',
        example='male',
    )
    user_name = Field(
        String(50),
        unique=True,
        required=True,
        not_none=True,
        readonly=False,
        label='User Name',
        example='ali_ahmadi',
    )
    email = Field(
        String,
        unique=True,
        required=True,
        not_none=True,
        readonly=False,
        label='Email',
        example='ali@gmail.com',
    )
    _password = Field(
        'password',
        Unicode(128),
        index=True,
        protected=True,
        json='password',
        pattern=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+$',
        pattern_description='Password must include at least one uppercase, one'
                            'lowercase and one number',
        example='ABCabc123',
        watermark=None,
        label='Password',
        message=None,
        min_length=6,
        max_length=20,
        required=True,
        python_type=str,
        not_none=True,
    )
    birth_date = Field(
        Date,
        python_type=datetime.date,
        label='Birth Date',
        pattern=r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])',
        pattern_description='ISO format like "yyyy-mm-dd" is valid',
        example='2018-02-02',
        watermark='Birth Date',
        nullable=True,
        not_none=False,
        required=False,
        readonly=False,
    )

    events = relationship(
        'Event',
        back_populates='creator',
        cascade='all, delete',
    )
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

