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

    bot_event = Event(
        title='event1',
        description='event1',
        bot=bot
    )
    session.add(bot_event)

    channel_event = Event(
        title='event1',
        description='event1',
    )
    session.add(channel_event)

    channel.event = channel_event

    assert bot_event.owner == bot
    assert bot_event.id == bot.event.id
    assert bot_event == bot.event

    assert channel_event.owner == channel
    assert channel_event.id == channel.event.id

