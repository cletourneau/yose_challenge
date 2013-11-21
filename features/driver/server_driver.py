import socket
import subprocess
import time
from features.driver.ip_port_in_use_matcher import in_use

from hamcrest import assert_that, is_not


class ServerDriver(object):
    def __init__(self, name, port=8000, ip_address='0.0.0.0'):
        self.name = name
        self.port = port
        self.ip_address = ip_address
        self.proc = None

    def start(self, cmd, **kwargs):
        assert_that((self.ip_address, self.port), is_not(in_use()))

        self.proc = subprocess.Popen(cmd, **kwargs)
        self._wait_until_port_is_opened(self.port)

    def shutdown(self):
        self.proc.terminate()
        print "========== Begin {server_name} server Output ==========".format(server_name=self.name)
        print self.proc.communicate()[0]
        print "=========== End {server_name} Output ===========".format(server_name=self.name)

    def _run_and_wait(self, command, working_dir):
        print 'waiting for <' + command + '> in ' + working_dir
        subprocess.check_call(command, cwd=working_dir, shell=True)

    def _wait_until_port_is_opened(self, port):
        for _ in range(0, 10):
            host = '127.0.0.1'
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                my_socket.connect((host, port))
                my_socket.close()
                break
            except socket.error:
                time.sleep(1)