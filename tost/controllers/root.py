from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin


class Apiv1(RestController, JSONPatchControllerMixin):
    pass


class Root(RootController):
    apiv1 = Apiv1()

