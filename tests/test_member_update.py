from datetime import date

from bddrest import status, when, given, response

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

    def test_update(self):
        user_name = 'member3'
        email = 'member3@mail.com'
        first_name = 'member3'
        last_name = 'falahi'

        with self.given(
            'update member',
            f'/apiv1/members/id:{self.member1.id}',
            'UPDATE',
            json=dict(
                userName=user_name,
                email=email,
                firstName=first_name,
                lastName=last_name,

            ),
        ):
            assert status == 200
            assert response.json['id'] == self.member1.id
            assert response.json['userName'] == user_name
            assert response.json['email'] == email
            assert response.json['firstName'] == first_name
            assert response.json['lastName'] == last_name

            when(
                'Trying to pass duplicate username',
                json=given | dict(userName=self.member2.user_name),
            )
            assert status == '400 Username is already exist'

            when('Trying to pass empty username', json=given - 'userName',)
            assert status == '400 Username is required'

            when(
                'Trying to pass Null username',
                json=given | dict(userName=None),
            )
            assert status == '400 Username is null'

            when(
                'Trying to pass less than 5 character',
                form=dict(userName='aq'),
            )
            assert status == '400 Username Length Must Be Greater Than 5 ' \
                             'Characters and Less than 20 Character'

            when(
                'Trying to pass greater than 20 character',
                form=dict(userName='a' * 21),
            )
            assert status == '400 Username Length Must Be Greater Than 5 ' \
                             'Characters and Less than 20 Character'

            when(
                'Trying to pass duplicate email',
                json=given | dict(email=self.member2.email),
            )
            assert status == '400 email address is already exist'

            when(
                'Trying to pass invalid email format',
                json=given | dict(email='asd.com'),
            )
            assert status == '400 Invalid Email Format'

            when(
                'Trying to pass Null email',
                json=given | dict(email=None),
            )
            assert status == '400 Email is null'

            when(
                'Trying to pass Null firstname',
                json=given | dict(firstName=None),
            )
            assert status == '400 Firstname field is null'

            when(
                'Trying to pass Null lastname',
                json=given | dict(lastName=None),
            )
            assert status == '400 Lastname field is null'

