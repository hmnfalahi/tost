from datetime import date

from bddrest import status, response

from tost.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member1 = Member(
            first_name='ali1',
            last_name='ahmadi1',
            user_name='aliahmadi1',
            email='ali1@gmail.com',
            gender='male',
            password='Abcd1234',
            birth_date=date(2000, 4, 9),
        )
        session.add(cls.member1)

        cls.member2 = Member(
            first_name='ali2',
            last_name='ahmadi2',
            user_name='aliahmadi2',
            email='ali2@gmail.com',
            gender='male',
            password='Abcd1234',
            birth_date=date(2000, 4, 9),
        )
        session.add(cls.member2)
        session.commit()

    def test_delete(self):

        with self.given(
            'delete member',
            f'/apiv1/members/id: {self.member1.id}',
            'DELETE',
        ):
            assert status == 200
            assert response.json['id'] == self.member1.id
            assert response.json['userName'] == self.member1.user_name
            assert response.json['email'] == self.member1.email
            assert response.json['firstName'] == self.member1.first_name
            assert response.json['lastName'] == self.member1.last_name

            session = self.create_session()
            assert not session.query(Member) \
                .filter(Member.id == self.member1.id) \
                .one_or_none()

