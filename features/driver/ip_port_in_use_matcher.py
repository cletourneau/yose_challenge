import socket
from hamcrest.core.base_matcher import BaseMatcher


class IpPortInUseMatcher(BaseMatcher):

    def __init__(self):
        super(IpPortInUseMatcher, self).__init__()
        self.ip_address = None
        self.port = None

    def _matches(self, item):
        self.ip_address, self.port = item
        return self._port_in_use()

    def _port_in_use(self):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = socket.timeout
        socket.timeout = 1
        try:
            my_socket.connect((self.ip_address, self.port))
            return True
        except socket.error:
            return False
        finally:
            my_socket.close()
            socket.timeout = timeout

    def describe_to(self, description):
        description.append_text('{ip}:{port} in use'.format(ip=self.ip_address, port=self.port))

    def describe_mismatch(self, item, mismatch_description):
        ip, port = item
        mismatch_description.append_text('{ip}:{port} not in use'.format(ip=ip, port=port))


def in_use():
    return IpPortInUseMatcher()