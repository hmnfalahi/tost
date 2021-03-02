from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        user_name = 'hmnfalahi'
        email = 'hmnfalahi@mail.co'
        first_name = 'hmn'
        last_name = 'falahi'
        gender = 'male'
        birth_date = '1999-08-07'
        password = 'Hhmnfalahi9964'

        with self.given(
                'Create a member',
                '/apiv1/members',
                'CREATE',
                json=dict(
                    userName=user_name,
                    email=email,
                    gender=gender,
                    firstName=first_name,
                    lastName=last_name,
                    birthDate=birth_date,
                    password=password,
                ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['userName'] == user_name
            assert response.json['email'] == email
            assert response.json['gender'] == gender
            assert response.json['firstName'] == first_name
            assert response.json['lastName'] == last_name
            assert response.json['birthDate'] == birth_date

            when('Trying to pass without form parameters', json={})
            assert status == '400 No Parameter Exists In The Form'

            when(
                'Trying to pass null username',
                json=given | dict(userName=None),
            )
            assert status == '400 Username is null'

            when('Trying to pass empty username', json=given - 'userName')
            assert status == '400 Username is required'

            when('Trying to pass null username', json=given | dict(email=None))
            assert status == '400 Email is null'

            when('Trying to pass empty email', json=given - 'email')
            assert status == '400 Email Not In Form'

            when(
                'Trying to pass less than 5 character',
                json=given | dict(userName='aq'),
            )
            assert status == '400 Username Length Must Be Greater Than 5 ' \
                'Characters and Less than 20 Character'

            when(
                'Trying to pass greater than 20 character',
                json=given | dict(userName='a' * 22),
            )
            assert status == '400 Username Length Must Be Greater Than 5 ' \
                'Characters and Less than 20 Character'

            when(
                'Trying to pass greater than 20 character',
                json=given - 'gender',
            )
            assert status == '400 Gender is required'

            when(
                'Trying to pass greater than 20 character',
                json=given | dict(gender=None),
            )
            assert status == '400 Gender is null'

            when(
                'Trying to pass null firstname',
                json=given | dict(firstName=None),
            )
            assert status == '400 Firstname field is null'

            when(
                'Trying to pass null lastname',
                json=given | dict(lastName=None),
            )
            assert status == '400 Lastname field is null'

