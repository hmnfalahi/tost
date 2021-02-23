from bddrest import status, response

from tost.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member1 = Member(
            email='hmn1@gmail.com',
            user_name='hmn1',
            first_name='hmn1',
            last_name='falahi',
            password='Hhmnfalahi9964',
        )
        session.add(cls.member1)

        cls.member2 = Member(
            email='hmn2@gmail.com',
            user_name='hmn2',
            first_name='hmn2',
            last_name='falahi',
            password='Hhmnfalahi9964',
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

