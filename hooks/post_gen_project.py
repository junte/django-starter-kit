'''
NOTE:
    the below code is to be maintained Python 2.x-compatible
    as the whole Cookiecutter Django project initialization
    can potentially be run in Python 2.x environment
    (at least so we presume in `pre_gen_project.py`).
TODO: ? restrict Cookiecutter Django project initialization to Python 3.x environments only
'''
from __future__ import print_function

import os
import random
import shutil

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = '\x1b[0m'
WARNING = '\x1b[1;33m [WARNING]: '
INFO = '\x1b[1;33m [INFO]: '
HINT = '\x1b[3;33m'
SUCCESS = '\x1b[1;32m [SUCCESS]: '


def remove_docker_files():
    shutil.rmtree('docker')

    file_names = ['.dockerignore']
    for file_name in file_names:
        os.remove(file_name)


def remove_gitlab_ci_files():
    file_names = ['.gitlab-ci.yml']
    for file_name in file_names:
        os.remove(file_name)


def remove_celery_files():
    file_names = [
        os.path.join('server', 'celery_app.py'),
    ]
    for file_name in file_names:
        os.remove(file_name)


def remove_drf_files():
    shutil.rmtree(os.path.join('server', 'apps', 'users', 'rest'), )
    shutil.rmtree(os.path.join('server', 'apps', 'core', 'rest'), )
    file_names = [
        os.path.join('tests', 'test_users', 'test_api_login.py'),
        os.path.join('tests', 'test_users', 'test_api_logout.py'),
        os.path.join('tests', 'test_users', 'test_api_me_user.py'),
        os.path.join('tests', 'test_users', 'test_api_users.py'),
    ]
    for file_name in file_names:
        os.remove(file_name)


def prepare_for_run():
    shutil.copy(
        os.path.join('server', 'settings', 'environments', 'development.py.example'),
        os.path.join('server', 'settings', 'environments', 'development.py'),
    )


def main():
    if '{{ cookiecutter.use_docker }}'.lower() == 'n':
        remove_docker_files()

    if '{{ cookiecutter.use_drf }}'.lower() == 'n':
        remove_drf_files()

    if '{{ cookiecutter.use_gitlab_ci }}'.lower() == 'n':
        remove_gitlab_ci_files()

    if '{{ cookiecutter.use_celery }}'.lower() == 'n':
        remove_celery_files()

    prepare_for_run()

    print(SUCCESS + 'Project initialized, keep up the good work!' + TERMINATOR)


if __name__ == '__main__':
    main()
