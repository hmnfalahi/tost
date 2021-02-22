from restfulpy.testing import db

from tost.models import Bot
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

    bot = Bot(
        name='bot1',
        title='bot_title',
        owner_id=member.id,
    )
    session.add(bot)
    session.commit()

    assert bot.id is not None
    assert bot.name == 'bot1'
    assert bot.title == 'bot_title'
    assert bot.owner_id == member.id

