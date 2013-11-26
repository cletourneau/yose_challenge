from fabric.context_managers import lcd
from fabric.decorators import task
from fabric.operations import local
from features.driver.server_driver import ServerDriver

VIRTUALENV = '.py27'


@task(default=True)
def default():
    test()


@task
def setup():
    install_python_requirements()
    install_node_requirements()


@task
def deploy():
    local('git push dokku master')


@task
def install_python_requirements():
    local('pip install -r requirements.txt --use-mirrors')
    local('pip install -r requirements-test.txt --use-mirrors')


@task
def install_node_requirements():
    with lcd('node'):
        local('npm install')


@task
def unit():
    local("nosetests -a '!needs_server'")


@task
def test():
    with YoseServer(port=8080):
        local("nosetests --tc=server_url:'http://localhost:8080'")
        local('killall phantomjs')


@task
def run_server():
    local("python -c 'import yose; yose.APP.run(port=8080)'")


class YoseServer():
    def __init__(self, port=8080):
        self.port = port
        self.server = ServerDriver(name='Yose', port=self.port)

    def __enter__(self):
        self.server.start(cmd=['gunicorn', 'yose:APP', '-w', '1', '-b', '0.0.0.0:{0}'.format(self.port)])
        return self.server

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.shutdown()