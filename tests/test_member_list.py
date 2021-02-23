from bddrest import status, response, when

from tost.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        member1 = Member(
            email='hmn1@gmail.com',
            user_name='hmn1',
            first_name='hmn',
            last_name='falahi',
            password='ABc123123',
        )
        session.add(member1)

        member2 = Member(
            email='hmn2@gmail.com',
            user_name='hmn2',
            first_name='hmn',
            last_name='falahi',
            password='ABc123123',
        )
        session.add(member2)

        member3 = Member(
            email='hmn3@gmail.com',
            user_name='hmn3',
            first_name='hmn',
            last_name='falahi',
            password='ABc123123',
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
            assert response.json[0]['id'] < response.json[1]['id']

