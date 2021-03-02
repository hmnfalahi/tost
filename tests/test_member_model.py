from datetime import date

from restfulpy.testing import db

from tost.models.member import Member


def test_age(db):
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

    assert member.members_count == 1
    assert member.id is not None
    assert member.birth_date.isoformat() == '2000-04-09'
    assert member.age == 21

