from restfulpy.orm import DBSession

from tost.models import Bot, Member


def insert():
    god = Member(
        user_name='GOD',
        email='godmail@mail.com',
        first_name='god',
        last_name='godian',
        password='Abc123Rew',
    )
    DBSession.add(god)

    member1 = Member(
        user_name='member1',
        email='member1@mail.com',
        first_name='member1',
        last_name='family member1',
        password='Abc123Rew',
    )
    DBSession.add(member1)

    member2 = Member(
        user_name='member2',
        email='member2@mail.com',
        first_name='member2',
        last_name='family member1',
        password='Abc123Rew',
    )
    DBSession.add(member2)
    DBSession.commit()

    bot1 = Bot(
        name='bot',
        title='bot-title',
        owner_id=member1.id,
    )
    DBSession.add(bot1)
    DBSession.commit()

    print('Following member has been added:')
    print(god.user_name)

