from datetime import date

from bddrest import status, response

from tost.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member = Member(
            first_name='ali1',
            last_name='ahmadi1',
            user_name='aliahmadi1',
            email='ali1@gmail.com',
            gender='male',
            password='Abcd1234',
            birth_date=date(2000, 4, 9),
        )
        session.add(cls.member)
        session.commit()

    def test_get(self):
        with self.given(
            'get member',
            f'/apiv1/members/id:{self.member.id}',
            'GET',
        ):
            assert status == 200
            assert response.json['id'] == self.member.id
            assert response.json['userName'] == self.member.user_name
            assert response.json['email'] == self.member.email
            assert response.json['firstName'] == self.member.first_name
            assert response.json['lastName'] == self.member.last_name

