from datetime import date

from tost.models import Bot, Channel, Event, Member

from restfulpy.testing import db


def test_event(db):
    session = db()
    member = Member(
        first_name='ali',
        last_name='ahmadi',
        user_name='aliahmadi',
        email='ali@gmail.com',
        gender='male',
        password='Abcd1234',
        birth_date=date(2000, 4, 9),
    )
    session.add(member)
    session.flush()

    bot = Bot(
        name='bot1',
        title='bot1',
        owner_id=member.id,
    )
    session.add(bot)

    channel = Channel(
        name='channel1',
        title='channel1',
        owner_id=member.id,
    )
    session.add(channel)
    event1 = Event(
        title='event1',
        status='published',
        description='event1',
        creator=member,
    )
    session.add(event1)

    event2 = Event(
        title='event2',
        status='draft',
        description='event2',
        creator=member,
    )
    session.add(event2)
    session.commit()

    # Test Bot Event
    assert event1.id is not None
    assert event1.owner == None
    assert len(bot.events) == 0

    bot.events.append(event1)
    assert event1 in bot.events
    assert event1.owner == bot
    assert event1.id == bot.events[0].id

    # Test channel event
    assert event2.id is not None
    assert len(channel.events) == 0
    assert event2.owner is None

    channel.events.append(event2)
    assert event2.owner == channel
    assert event2.id == channel.events[0].id
    assert event2 in channel.events

    # Test event creator
    assert event1.creator_id == member.id
    assert event2.creator == member
    assert [event1, event2] == member.events

