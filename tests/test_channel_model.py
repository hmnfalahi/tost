from datetime import date

from restfulpy.testing import db

from tost.models import Channel
from tost.models import Member


def test_create(db):
    session = db()
    member = Member(
        first_name='ali1',
        last_name='ahmadi1',
        user_name='aliahmadi1',
        email='ali1@gmail.com',
        gender='male',
        password='Abcd1234',
        birth_date=date(2000, 4, 9),
    )
    session.add(member)
    session.commit()

    member2 = Member(
        first_name='ali2',
        last_name='ahmadi2',
        user_name='aliahmadi2',
        email='ali2@gmail.com',
        gender='male',
        password='Abcd1234',
        birth_date=date(2000, 4, 9),
    )
    session.add(member2)

    channel = Channel(
        name='channel1',
        title='channel1_title',
        owner_id=member.id,
        admins=[member],
    )
    session.add(channel)
    session.commit()

    member3 = Member(
        first_name='ali3',
        last_name='ahmadi3',
        user_name='aliahmadi3',
        email='ali3@gmail.com',
        gender='male',
        password='Abcd1234',
        birth_date=date(2000, 4, 9),
    )
    session.add(member3)
    session.commit()

    channel.admins.append(member3)

    assert channel.id is not None
    assert channel.name == 'channel1'
    assert channel.title == 'channel1_title'
    assert channel.owner_id == member.id
    assert channel.admins is not None
    assert member in channel.admins
    assert member2 not in channel.admins
    assert member3 in channel.admins

