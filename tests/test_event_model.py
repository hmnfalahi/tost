from tost.models import Bot, Channel, Event

from restfulpy.testing import db


def test_event(db):
    session = db()

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
        description='event1',
    )
    session.add(event1)

    event2 = Event(
        title='event2',
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
    #
    channel.events.append(event2)
    assert event2.owner == channel
    assert event2.id == channel.events[0].id
    assert event2 in channel.events

