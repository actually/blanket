import soaplib
from soaplib.core.service import soap, DefinitionBase
from soaplib.core.server import wsgi
from soaplib.core.model.primitive import String

from config import config

from product.validation import Validation

import logging

log = logging.getLogger(__name__)

class Blanket(DefinitionBase):
    """ Fabric SOAP Interface """

    @soap(String, _returns=String)
    def doNothing(self, auth_token):
        """ validate and reply. """
        Validation.checkAuth(auth_token)

        return 'nothing'

def run():
    from cherrypy.wsgiserver import CherryPyWSGIServer
    soap_application =  soaplib.core.Application([Blanket], 'blanket')
    wsgi_application = wsgi.Application(soap_application)
    server = CherryPyWSGIServer(('0.0.0.0', config.soap_port), wsgi_application)
    server.start()