import re

from nanohttp import json, validate, context, int_or_notfound, HTTPNotFound, \
    HTTPForbidden
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

