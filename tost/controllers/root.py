from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin

from .event import EventController
from .member import MemberController


class Apiv1(RestController, JSONPatchControllerMixin):
    members = MemberController()
    events = EventController()


class Root(RootController):
    apiv1 = Apiv1()

