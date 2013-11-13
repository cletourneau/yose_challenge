import sys
from fabric.context_managers import prefix
from fabric.decorators import task
from fabric.operations import local

VIRTUALENV = '.py27'


@task(default=True)
def default():
    test_py()


@task
def setup():
    local('virtualenv --distribute --python=python2.7 {env}'.format(env=VIRTUALENV))
    install_requirements()


@task
def install_requirements():
    with prefix(_activate_virtual_env()):
        local('pip install -r requirements.txt --use-mirrors')
        local('pip install -r requirements-test.txt --use-mirrors')


@task
def test_py():
    with prefix(_activate_virtual_env()):
        local('nosetests')


@task
def run_server():
    with prefix(_activate_virtual_env()):
        local("python -c 'import yose; yose.APP.run(port=8181)'")


def _activate_virtual_env():
    if not hasattr(sys, 'real_prefix'):
        return '. {env}/bin/activate'.format(env=VIRTUALENV)
    else:
        return 'true'