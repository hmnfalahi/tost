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
    assert bot.event == None

    bot.event = event1
    assert bot.event == event1
    assert event1.owner == bot
    assert event1.id == bot.event.id

    # Test channel event
    assert event2.id is not None
    assert channel.event is None
    assert event2.owner is None

    channel.event = event2
    assert event2.owner == channel
    assert event2.id == channel.event.id
    assert channel.event == event2

