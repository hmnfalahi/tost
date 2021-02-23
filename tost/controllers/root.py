from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin

from .member import MemberController


class Apiv1(RestController, JSONPatchControllerMixin):
    members = MemberController()


class Root(RootController):
    apiv1 = Apiv1()

