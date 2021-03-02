from datetime import date

from bddrest import status, response, when

from tost.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        member1 = Member(
            first_name='ali1',
            last_name='ahmadi1',
            user_name='aliahmadi1',
            email='ali1@gmail.com',
            gender='male',
            password='Abcd1234',
            birth_date=date(2000, 4, 9),
        )
        session.add(member1)

        member2 = Member(
            first_name='ali2',
            last_name='ahmadi2',
            user_name='aliahmadi2',
            email='ali2@gmail.com',
            gender='male',
            password='Abcd1234',
            birth_date=date(2000, 4, 9),
        )
        session.add(member2)

        member3 = Member(
            first_name='ali3',
            last_name='ahmadi3',
            user_name='aliahmadi3',
            email='ali3@gmail.com',
            gender='male',
            password='Abcd1234',
            birth_date=date(2000, 4, 9),
        )
        session.add(member3)
        session.commit()

    def test_list(self):

        with self.given(
            'get members list',
            '/apiv1/members',
            'LIST',
        ):
            assert status == 200
            assert len(response.json) == 3

            when('Trying to sorting response', query=dict(sort='id'))
            assert len(response.json) == 3
            index = 1
            while index < len(response.json):
                assert response.json[index - 1]['id'] < \
                   response.json[index]['id']
                index += 1

            when('Sorting the response descending', query=dict(sort='-id'))
            assert len(response.json) == 3
            assert response.json[0]['id'] > response.json[1]['id']

