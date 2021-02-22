from datetime import date

from tost.models.initial import Session
from tost.models import Member


class TestMember:
    @classmethod
    def setup_class(cls):
        cls.session = Session()
        cls.session.query(Member).delete()
        cls.session.commit()

    @classmethod
    def teardown_class(cls):
        cls.session.query(Member).delete()
        cls.session.commit()

    def test_age(self):
        session = Session()

        member1 = Member(
            user_name='ali',
            email='ali@gmail.com',
            password='ahmadi',
            birth_date=date(2000, 4, 9),
        )
        session.add(member1)

        member2 = Member(
            user_name='mohammad',
            email='mohammad@gmail.com',
            password='mohammadi',
            birth_date=date(2000, 4, 9),
        )
        session.add(member2)
        session.commit()

        count_of_members = session.query(Member).count()
        assert count_of_members == 2

        assert member1.id is not None
        assert member1.birth_date.isoformat() == '2000-04-09'
        assert member1.age == 21

