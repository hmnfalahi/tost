import re

from nanohttp import json, validate, context, int_or_notfound, HTTPNotFound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import commit, DBSession

from tost.models import Member
from ..exceptions import *


MEMBER_PASSWORD_PATTERN = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+')
MEMBER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)


class MemberController(ModelRestController):

    @json(
        prevent_empty_form='400 No Parameter Exists In The Form',
    )
    @validate(
        userName=dict(
            type_=(str, StatusInvalidStringType),
            min_length=(5, StatusUsernameLengthInvalid),
            max_length=(20, StatusUsernameLengthInvalid),
            required=StatusUsernameIsRequired,
            not_none=StatusUsernameIsNull,
        ),
        email=dict(
            required=StatusEmailIsRequired,
            not_none=StatusEmailIsNull,
            pattern=(MEMBER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
        firstName=dict(
            not_none=StatusFirstnameIsNull,
        ),
        lastName=dict(
            not_none=StatusLastnameIsNull,
        ),
        password=dict(
            required=HTTPPasswordNotInForm,
            not_none=HTTPPasswordIsNull,
            min_length=(6, HTTPPasswordInvalidLength),
            max_length=(20, HTTPPasswordInvalidLength),
            pattern=(MEMBER_PASSWORD_PATTERN, HTTPPasswordWrongPattern),
        ),
    )
    @commit
    def create(self):
        member_username_check = DBSession.query(Member) \
            .filter(Member.user_name == context.form.get('userName')) \
            .one_or_none()
        if member_username_check is not None:
            raise StatusRepetitiveUsername()

        member_email_check = DBSession.query(Member) \
            .filter(Member.email == context.form.get('email')) \
            .one_or_none()
        if member_email_check is not None:
            raise StatusRepetitiveEmail()

        member = Member()
        member.update_from_request()
        DBSession.add(member)
        return member
      
    @json
    def get(self, id):
        id = int_or_notfound(id)
        member = DBSession.query(Member).get(id)
        if member is None:
            raise HTTPNotFound()
        return member

    @json
    @Member.expose
    def list(self):
        members = DBSession.query(Member)
        return members

    @json
    @commit
    def delete(self, id):
        id = int_or_notfound(id)
        member = DBSession.query(Member).get(id)
        if member is None:
            raise HTTPNotFound()

        DBSession.delete(member)
        return member

    @json
    @validate(
        userName=dict(
            type_=(str, StatusInvalidStringType),
            min_length=(5, StatusUsernameLengthInvalid),
            max_length=(20, StatusUsernameLengthInvalid),
            required=StatusUsernameIsRequired,
            not_none=StatusUsernameIsNull,
        ),
        email=dict(
            not_none=StatusEmailIsNull,
            pattern=(MEMBER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
        firstName=dict(
            not_none=StatusFirstnameIsNull,
        ),
        lastName=dict(
            not_none=StatusLastnameIsNull,
        ),
    )
    @commit
    def update(self, id):
        id = int_or_notfound(id)
        user_name = context.form.get('userName')
        email = context.form.get('email')

        member = DBSession.query(Member) \
            .filter(Member.id == id) \
            .one_or_none()

        if member is None:
            raise HTTPNotFound()

        username_exists = DBSession.query(Member) \
            .filter(Member.user_name == user_name) \
            .filter(Member.id != id) \
            .one_or_none()

        if username_exists:
            raise StatusRepetitiveUsername()

        email_exist = DBSession.query(Member) \
            .filter(Member.email == email) \
            .filter(Member.id != id) \
            .one_or_none()

        if email_exist:
            raise StatusRepetitiveEmail()

        member.update_from_request()
        return member

