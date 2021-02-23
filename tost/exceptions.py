from nanohttp import HTTPKnownStatus, settings


class StatusInvalidStringType(HTTPKnownStatus):
    status = '400 Invalid type for username'


class StatusUsernameLengthInvalid(HTTPKnownStatus):
    status = '400 Username Length Must Be Greater Than 5' \
             ' Characters and Less than 20 Character'


class StatusUsernameIsRequired(HTTPKnownStatus):
    status = '400 Username is required'


class StatusUsernameIsNull(HTTPKnownStatus):
    status = '400 Username is null'


class StatusEmailIsRequired(HTTPKnownStatus):
    status = '400 Email Not In Form'


class StatusEmailIsNull(HTTPKnownStatus):
    status = '400 Email is null'


class StatusInvalidEmailFormat(HTTPKnownStatus):
    status = '400 Invalid Email Format'


class StatusFirstnameIsNull(HTTPKnownStatus):
    status = '400 Firstname field is null'


class StatusLastnameIsNull(HTTPKnownStatus):
    status = '400 Lastname field is null'


class HTTPPasswordNotInForm(HTTPKnownStatus):
    status = '400 Password Not In Form'


class HTTPPasswordIsNull(HTTPKnownStatus):
    status = '400 Password is null'


class HTTPPasswordInvalidLength(HTTPKnownStatus):
    status = '400 Invalid Password Length'


class HTTPPasswordWrongPattern(HTTPKnownStatus):
    status = '400 Password Not Complex Enough'


class StatusRepetitiveUsername(HTTPKnownStatus):
    status = '400 Username is already exist'


class StatusRepetitiveEmail(HTTPKnownStatus):
    status = '400 email address is already exist'

