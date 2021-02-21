from os.path import dirname

from nanohttp import settings
from restfulpy import Application


__version__ = '0.1'


class Tost(Application):
    __configuration__ = '''
      db:
        url: postgresql://postgres:postgres@localhost/tost
        test_url: postgresql://postgres:postgres@localhost/tost_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres
   '''

    def __init__(self, application_name='tost', root=None):
        super().__init__(
            application_name,
            root=root,
            root_path=dirname(__file__),
            version=__version__
        )

    @classmethod
    def initialize_orm(cls, engine=None):
        super().initialize_orm(cls, engine)


tost = Tost()

