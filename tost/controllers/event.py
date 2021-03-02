from nanohttp import validate, json, context, RestController
from restfulpy.orm import commit, DBSession

from tost.models import Event
from ..exceptions import *


class EventController(RestController):

    @json
    @validate(
        title=dict(
            type_=(str, StatusInvalidStringType),
            required=StatusTitleIsRequired,
            not_none=StatusTitleIsNull,
        ),
        status=dict(
            required=StatusStatusIsRequired,
            not_none=StatusStatusIsNull,
        ),
        description=dict(
            not_none=StatusDescriptionIsNull,
        ),
    )
    @commit
    def create(self):
        is_title_exists = DBSession.query(Event) \
            .filter(Event.title == context.form.get('title')) \
            .one_or_none()
        if is_title_exists is not None:
            raise StatusRepetitiveTitle()

        event = Event()
        event.update_from_request()
        DBSession.add(event)
        return event

