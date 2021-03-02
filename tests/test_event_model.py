from tost.models import Bot, Channel, Event, Member

from restfulpy.testing import db


def test_event(db):
    session = db()
    member = Member(
        user_name='member1',
        first_name='member',
        last_name='1',
        email='member1@mail.com',
        password='Abcd1234',
    )

    bot = Bot(
        name='bot1',
        title='bot1',
    )
    session.add(bot)

    channel = Channel(
        name='channel1',
        title='channel1',
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
    assert event2.creator is None

    member.events.append(event2)
    assert event2.creator is not None
    assert event2.creator == member
    assert [event1, event2] == member.events

