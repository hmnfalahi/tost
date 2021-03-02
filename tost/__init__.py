from os.path import dirname

from nanohttp import settings
from restfulpy import Application

from .controllers.root import Root
from . import basedata
from . import mockup


__version__ = '0.1'


class Tost(Application):
    __configuration__ = '''
      db:
        url: postgresql://postgres:postgres@localhost/tost
        test_url: postgresql://postgres:postgres@localhost/tost_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres
   '''

    def __init__(self, application_name='tost', root=Root()):
        super().__init__(
            application_name,
            root=root,
            root_path=dirname(__file__),
            version=__version__,
        )

    def insert_basedata(self, *args):
        basedata.insert()

    def insert_mockup(self, *args):
        mockup.insert()

    @classmethod
    def initialize_orm(cls, engine=None):
        super().initialize_orm(cls, engine)


tost = Tost()

