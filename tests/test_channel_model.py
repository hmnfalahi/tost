from restfulpy.testing import db

from tost.models import Channel
from tost.models import Member


def test_create(db):
    session = db()
    member = Member(
        first_name='ali1',
        email='ali1@gmail.com',
        last_name='ahmadi',
        user_name='ali',
        password='9964',
    )
    session.add(member)
    session.commit()

    member2 = Member(
        first_name='ali2',
        email='ali2@gmail.com',
        last_name='ahmadi',
        user_name='ali2',
        password='9964',
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
        email='ali3@gmail.com',
        last_name='ahmadi',
        user_name='ali3',
        password='9964',
        channels=[channel],
    )
    session.add(member3)
    session.commit()

    assert channel.id is not None
    assert channel.name == 'channel1'
    assert channel.title == 'channel1_title'
    assert channel.owner_id == member.id
    assert channel.admins is not None
    assert member in channel.admins
    assert member2 not in channel.admins
    assert member3 in channel.admins

