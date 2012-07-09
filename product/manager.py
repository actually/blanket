from soaplib.core.service import soap
from soaplib.core.server.wsgi import Application
from soaplib.core.model.primitive import String

from config import config

from product.validation import Validation

import logging

log = logging.getLogger(__name__)

class Blanket(Application):
    """ Fabric SOAP Interface """

    @soap(String, _returns=String)
    def doNothing(self, auth_token):
        """ validate and reply. """
        Validation.checkAuth(auth_token)

        return 'nothing'

def run():
    from cherrypy.wsgiserver import CherryPyWSGIServer
    server = CherryPyWSGIServer(('0.0.0.0', config.soap_port), Blanket())
    server.start()