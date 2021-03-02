from restfulpy.orm import DBSession

from tost.models import Bot, Channel, Member


def insert():
    member1 = Member(
        user_name='mockmember1',
        email='mail1@mail.com',
        first_name='mockmember1',
        last_name='family member1',
        password='Abc123Rew',
    )
    DBSession.add(member1)

    member2 = Member(
        user_name='mockmember2',
        email='mail2@mail.com',
        first_name='mockmember2',
        last_name='family member2',
        password='Abc123Rew',
    )
    DBSession.add(member2)

    member3 = Member(
        user_name='mockmember3',
        email='mail3@mail.com',
        first_name='mockmember3',
        last_name='family member3',
        password='Abc123Rew',
    )
    DBSession.add(member3)
    DBSession.commit()

    bot1 = Bot(
        name='bot',
        title='bot-title',
        owner_id=member1.id,
    )
    DBSession.add(bot1)

    bot2 = Bot(
        name='bot2',
        title='bot2-title',
        owner_id=member1.id,
    )
    DBSession.add(bot2)

    bot3 = Bot(
        name='bot3',
        title='bot3-title',
        owner_id=member1.id,
    )
    DBSession.add(bot3)
    DBSession.commit()

    channel1 = Channel(
        name='channel1',
        title='channel1-title',
        owner_id=member1.id,
        admins=[
            member2,
            member3,
        ],
    )
    DBSession.add(channel1)
    DBSession.commit()

