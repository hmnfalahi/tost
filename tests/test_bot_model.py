from datetime import date

from restfulpy.testing import db

from tost.models import Bot
from tost.models import Member


def test_create(db):
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

