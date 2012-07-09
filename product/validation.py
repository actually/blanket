from config import config

class Validation:
    """ Various methods for input validation. """

    @staticmethod
    def checkAuth(auth_token):
        """ Verify that submitted token matches. """
        if (auth_token != config.token):
            raise Exception("Authentication Failed")

    @staticmethod
    def checkHost(host):
        """ Check that submitted p4 port is included in the valid list. """
        if host not in config.valid_hosts:
            raise Exception("Invalid Server")

    @staticmethod
    def checkUser(user):
        """ Make sure protected users can no be modified. """
        if user in config.protected_users:
            raise Exception("Protected user " + user + \
                            " can not be modified")